# import random
# import discord
# from .button import create_view
# # from discord import Button

# from rps.model import RPS
# from rps.parser import Parser
# from rps.controller import RPSGame

# from types import NoneType
# from common.cfg import devguilds
# from discord.commands import slash_command

# class Rockpaperscissors(discord.Cog):
#     """Handles simple commands and listeners."""

#     def __init__(self, bot):
#         self.bot = bot

#     @slash_command(name="rps", guild_ids=devguilds)
#     async def rps(self, ctx, user_choice: Parser = Parser(RPS.ROCK)):
#         """Commmand to call rock paper scissors."""
#         if ctx.author.bot:
#             return

#         game_instance = RPSGame()

#         user_choice = user_choice.choice

#         winner, bot_choice = game_instance.run("asd")

#         if winner is None:
#             message = "It's a draw! Both chose: %s" % user_choice
#         elif winner is True:
#             message = "You win: %s vs %s" % (user_choice, bot_choice)
#         elif winner is False:
#             message = "You lose: %s vs %s" % (user_choice, bot_choice)

#         await ctx.send(message)

#         # view = discord.ui.View(RockButton(), PaperButton(), ScissorButton(), timeout=60)

#         # view = create_view()
#         # await ctx.respond(embed=game_instance, view=view)

# def setup(bot):
#     """Entry point for loading cogs. Required for all cogs"""
#     bot.add_cog(Rockpaperscissors(bot))