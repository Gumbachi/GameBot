"""Holds the queue class for the music player."""
import discord
from cogs.music.song import Song
from common.utils import normalize_time
from .buttons import *
from discord.ui import View
import keys

FFMPEG_OPTS = {
    "executable": keys.FFMPEG_PATH,
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}


class MusicPlayer():
    """A player class with 1 belonging to each guild"""

    def __init__(self, guild):
        self.guild = guild

        self.repeat_type = RepeatType.REPEATOFF
        self.paused = False
        self.current = None
        self.next = None
        self.songlist = []

    @property
    def playing(self):
        return not self.paused

    @property
    def empty(self):
        return len(self.songlist) == 0

    @property
    def embed(self) -> discord.Embed:

        if not self.current:
            return discord.Embed(title="No Songs Playing")

        embed = discord.Embed(
            title="NOW PLAYING",
            description=f"[{self.current.title}]({self.current.webpage_url})\n{normalize_time(self.current.duration)}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=self.current.thumbnail)

        if self.next:
            embed.add_field(name="UP NEXT", value=f"{self.next.title}")

        return embed

    @property
    def controller(self) -> discord.ui.View:
        play_button = PlayButton(self) if self.paused else PauseButton(self)
        skip_button = SkipButton(self)

        if self.repeat_type == RepeatType.REPEAT:
            repeat_button = RepeatButton(self)
        elif self.repeat_type == RepeatType.REPEATONE:
            repeat_button = RepeatOneButton(self)
        else:
            repeat_button = RepeatOffButton(self)

        return View(repeat_button, play_button, skip_button, timeout=None)

    def enqueue(self, song: Song):
        self.songlist.append(song)

    async def play_next(self):

        print(f"PLAYING NEXT: {self.repeat_type} {self.songlist}")

        if self.empty and self.current is None:
            await self.guild.voice_client.disconnect()
            return

        # Repeat one should loop current song
        if self.repeat_type == RepeatType.REPEATONE:
            # do nothing because current will be played again
            pass

        # Repeat should loop the entire list
        elif self.repeat_type == RepeatType.REPEAT:
            self.current = self.songlist.pop(0)
            self.songlist.append(self.current)

        # Repeat off should just burn through the songs
        else:
            self.current = self.songlist.pop(0)

        print(f"PLAYING: {self.current.title}")

        # Play the song
        audio = discord.FFmpegPCMAudio(self.current.url, **FFMPEG_OPTS)
        self.guild.voice_client.play(audio)
        self.paused = False

    def resume(self):
        self.paused = False
        self.guild.voice_client.resume()

    def pause(self):
        self.paused = True
        self.guild.voice_client.pause()

    async def skip(self):
        self.guild.voice_client.stop()
        await self.play_next()
