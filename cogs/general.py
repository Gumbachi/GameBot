import discord
import random
import asyncio
from cogs.rps.rps import RPSGame
from rps import RPS
from rps import Parser
from rps import RPSGame
from common.cfg import devguilds
from discord.commands import slash_command
from button import create_view


class GeneralCommands(discord.Cog):
    """Handles simple commands and listeners."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="howdy", guild_ids=devguilds)
    async def howdy(self, ctx):
        """Command to check if bot is alive or if you need a friend."""
        await ctx.respond(f"Howdy {ctx.author.mention}!")

    @staticmethod
    def playRPS():
        game_instance = RPSGame()

        user_choice = user_choice.choice

        winner, bot_choice = game_instance.run("asd")

        if winner is None:
            message = "It's a draw! Both chose: %s" % user_choice
        elif winner  is True:
            message = "You Win! %s vs %s" % (user_choice, bot_choice)
        elif winner is False:
            message = "You Lost! %s vs %s" % (user_choice, bot_choice)

        return message

    @slash_command(name="rps", guild_ids=devguilds)
    async def rps(self, ctx, user_choice: Parser = Parser(RPS.ROCK)):
        """Commmand to call rock paper scissors."""
        if ctx.author.bot:
            return

        game_instance = self.playRPS()

        view = create_view()
        await ctx.respond(embed=game_instance, view=view)


    @discord.Cog.listener()
    async def on_message(self, message):
        """Called for every message sent that the bot can see"""

        # Ignore bot messages
        if message.author.bot:
            return

        if message.content.lower() == "brian":
            await message.reply("hall")

    @discord.Cog.listener()
    async def on_guild_join(self, guild):
        """Bot has joined a guild."""
        print(f"Joined {guild.name}")

    @discord.Cog.listener()
    async def on_guild_remove(self, guild):
        """Bot is kicked/removed."""
        print(f"Left {guild.name}")


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(GeneralCommands(bot))
