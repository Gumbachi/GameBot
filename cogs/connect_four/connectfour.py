import discord
from common.cfg import devguilds
from discord.commands import slash_command, Option


class ConnectFour(discord.Cog):
    """Handles simple commands and listeners."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="connect4", guild_ids=devguilds)
    async def begin_connect4(
        self,
        ctx: discord.ApplicationContext,
        opponent: Option(discord.Member, description="Player 2")
    ):
        """Begin a game of Connect Four with a friend."""
        await ctx.respond(f"Howdy {ctx.author.mention}!")


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(ConnectFour(bot))
