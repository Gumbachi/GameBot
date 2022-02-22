import discord
from common.cfg import devguilds
from discord.commands import slash_command
import yt_dlp


class MusicPlayer(discord.Cog):
    """Handles simple commands and listeners."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="play", guild_ids=devguilds)
    async def play(self, ctx, song: str):
        """Command to start the music player."""
        await ctx.respond(f"In progress!")

    @slash_command(name="disconnect", guild_ids=devguilds)
    async def dc(self, ctx, song: str):
        """Command to start the music player."""
        await ctx.respond(f"In progress!")


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(MusicPlayer(bot))


def fetch_song(query: str):
    pass
