import discord
from common.cfg import devguilds
from discord.commands import slash_command
from .game import Game


class Minesweeper(discord.Cog):
    """Handles simple commands and listeners."""

    def __init__(self, bot):
        self.bot = bot
        self.instances = {}

    @slash_command(name="minesweeper", guild_ids=devguilds)
    async def start_minesweeper(
        self,
        ctx: discord.ApplicationContext
    ):
        """Begin a game of Minesweeper"""

        game = Game()
        self.instances[ctx.guild.id] = game
        await ctx.respond(content=f"```{game}```", view=game.view)


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(Minesweeper(bot))
