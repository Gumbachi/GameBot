import os
import time
import discord
from common.cfg import devguilds
from discord.commands import slash_command
from yt_dlp import YoutubeDL
from common.cfg import TENOR, EMOJI
import keys

YDL_OPTS = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # bind to ipv4
}

FFMPEG_OPTS = {
    "executable": keys.FFMPEG_PATH,
    # "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}


class MusicPlayer(discord.Cog):
    """Handles simple commands and listeners."""

    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def fetch_song(query: str) -> dict:
        with YoutubeDL(YDL_OPTS) as ydl:
            song_info = ydl.extract_info(f"ytsearch:{query}", download=False)
            try:
                data = song_info["entries"][0]
            except KeyError:
                return None  # Couldnt find song

            required_data = ("url", "title", "duration",
                             "thumbnail", "webpage_url")
            return {k: data[k] for k in required_data}

    @staticmethod
    def generate_player(song: dict) -> discord.Embed:
        player = discord.Embed(
            title="NOW PLAYING",
            description=f"[{song['title']}]({song['webpage_url']})\n{normalize_time(song['duration'])}",
            color=discord.Color.blue()
        )
        player.set_thumbnail(url=song["thumbnail"])

        player.add_field(
            name="UP NEXT",
            value=f"[{song['TBD']}]({song['webpage_url']}\nETA: 1:23:45"
        )

        return player

    @slash_command(name="connect", guild_ids=devguilds)
    async def connect_to_voice(self, ctx):
        """Connect to your voice channel"""
        # user is not in voice channel
        if not ctx.author.voice:
            return await ctx.respond(TENOR.KERMIT_LOST)

        # user is in different voice channel
        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
        else:
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
    async def play(self, ctx, songquery: str):
        """Command to start the music player."""

        song = self.fetch_song(songquery)
        audio = discord.FFmpegPCMAudio(song["url"], **FFMPEG_OPTS)

        ctx.voice_client.play(audio)

        await ctx.respond(f"Playing {song['title']}")


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    if not os.path.isfile(keys.FFMPEG_PATH):
        raise FileNotFoundError("Couldn't locate FFMPEG executable")

    bot.add_cog(MusicPlayer(bot))


def normalize_time(seconds: int):
    """Turns seconds into H:M:S"""
    if seconds < 3600:
        return time.strftime("%M:%S", time.gmtime(seconds))
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
