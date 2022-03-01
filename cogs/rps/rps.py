import discord

from .button import RockButton
from .button import PaperButton
from .button import ScissorButton

from common.cfg import devguilds
from discord.commands import slash_command

class RPSClass:
    def __init__(self):
        self.rock = set()
        self.paper = set()
        self.scissors = set()

    @property
    def embed(self):
         return discord.Embed(
            title="Choose Rock, Paper or Scissors",
            color=discord.Color.blue()
         )

    @property
    def controller(self):
        return discord.ui.View(RockButton(self), PaperButton(self), ScissorButton(self), timeout=60)

class Rockpaperscissors(discord.Cog):
    """Play Rock Paper Scissors"""

    def __init__(self, bot):
        self.bot = bot
        self.playerchoice = {}

    def get_choice(self, message):
        return self.playerchoice.get(message.id)

    @slash_command(name="rps", guild_ids=devguilds)
    async def rps(self, ctx):
        """Command to check if bot is alive or if you need a friend."""
        choice = RPSClass()
        message = await ctx.respond(embed=choice.embed, view=choice.controller)
        self.playerchoice[message.id] = choice


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(Rockpaperscissors(bot))
