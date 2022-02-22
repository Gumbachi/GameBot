import discord
from common.cfg import devguilds
from discord.commands import slash_command
from yt_dlp import YoutubeDL
from common.cfg import TENOR, EMOJI
import keys

YDL_OPTS = {
    "format": "bestaudio/best",
    "extractaudio": True,
    "audioformat": "mp3",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
}

FFMPEG_OPTS = {
    "executable": keys.FFMPEG_PATH,
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}


class MusicPlayer(discord.Cog):
    """Handles simple commands and listeners."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="connect", guild_ids=devguilds)
    async def connect_to_voice(self, ctx):
        """Connect to your voice channel"""
        # user is not in VC
        if not ctx.author.voice:
            return await ctx.respond(TENOR.KERMIT_LOST)

        await ctx.author.voice.channel.connect()
        return await ctx.respond(EMOJI.CHECK)

    @slash_command(name="disconnect", guilds_ids=devguilds)
    async def disconnect_from_voice(self, ctx):
        """Disconnect bot from your voice channel"""
        if not ctx.voice_client:
            return await ctx.respond(EMOJI.WEIRDCHAMP)

        await ctx.voice_client.disconnect()
        await ctx.respond(EMOJI.CHECK)

    @slash_command(name="play", guild_ids=devguilds)
    async def play(self, ctx, song: str):
        """Command to start the music player."""
        await ctx.respond(f"In progress!")


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(MusicPlayer(bot))


def fetch_song(query: str):
    pass
