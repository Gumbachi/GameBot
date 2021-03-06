import os

import discord
from discord import ApplicationContext as Context
from discord.commands import Option
from discord.commands import slash_command
from discord.ext import tasks
from discord.ext.commands import CommandError

import keys
from common.cfg import Emoji, Tenor, devguilds
from .player import MusicPlayer
from .song import Song


class Music(discord.Cog):
    """Handles simple commands and listeners."""

    def __init__(self, bot):
        self.bot = bot
        self.players = {}
        self.player_loop.start()

    def get_player(self, guild: discord.Guild) -> MusicPlayer:
        """Return active player or make a new one."""

        try:
            return self.players[guild.id]
        except KeyError:
            player = MusicPlayer(guild)
            self.players[guild.id] = player
            return player

    @staticmethod
    async def connect_to_voice(ctx):
        """Connect to your voice channel"""
        # user is not in voice channel
        if not ctx.author.voice:
            raise CommandError("You aren't in a voice channel")

        # user is in different voice channel
        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
        else:
            await ctx.author.voice.channel.connect()

    @slash_command(name="disconnect", guild_ids=devguilds)
    async def disconnect_from_voice(self, ctx):
        """Disconnect bot from your voice channel"""
        if not ctx.voice_client:
            return await ctx.respond(Emoji.WEIRDCHAMP)

        await ctx.voice_client.disconnect()
        del self.players[ctx.guild.id]
        await ctx.respond(Emoji.CHECK)

    @slash_command(name="play", guild_ids=devguilds)
    async def play(self, ctx: Context, song: Option(str, "Search for a song on youtube")):
        """Command to start the music player"""

        # Need to defer response since it takes time
        await ctx.interaction.response.defer()

        try:
            await self.connect_to_voice(ctx)
        except CommandError:
            return await ctx.respond(Tenor.KERMIT_LOST)

        song = Song.from_query(song)
        mp = self.get_player(ctx.guild)
        mp.enqueue(song)

        # Add to queue if there is already something playing
        if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
            emb = discord.Embed(title="Added to queue", description=song.title)
            emb.set_thumbnail(url=song.thumbnail)
            return await ctx.respond(embed=emb)

        await mp.play_next()
        message = await ctx.send(embed=mp.embed, view=mp.controller)
        mp.message = message
        await ctx.respond(message.jump_url)

    @slash_command(name="player", guild_ids=devguilds)
    async def send_player(self, ctx: Context):
        """Get the music player and its buttons."""

        mp = self.get_player(ctx.guild)
        mp.message = await ctx.send(embed=mp.embed, view=mp.controller)
        await ctx.respond(mp.message.jump_url)

    @tasks.loop(seconds=5)
    async def player_loop(self):
        """Checks the voice clients to see if one can go to next song"""
        for client in self.bot.voice_clients:

            # Voice client is already playing or paused so skip it
            if client.is_playing() or client.is_paused():
                continue

            mp = self.get_player(client.guild)
            await mp.play_next()

    @player_loop.before_loop
    async def before_player_loop(self):
        await self.bot.wait_until_ready()  # Wait until the bot logs in


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    if keys.FFMPEG_PATH != "ffmpeg" and not os.path.isfile(keys.FFMPEG_PATH):
        raise FileNotFoundError("Couldn't locate FFMPEG executable")

    bot.add_cog(Music(bot))
