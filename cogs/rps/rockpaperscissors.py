# THIS FILE's PURPOSE IS A ONE FILE WORKING VERSION OF RPS
# 
# import discord
# import random as rand
# from common.cfg import devguilds
# from discord.commands import slash_command
# from discord import ButtonStyle, Embed
# from typing import Optional
# from common.cfg import EMOJI

# class RockButton(discord.ui.Button):
#     def __init__(self, playerchoice):
#         """Play Rock"""
#         super().__init__(emoji=EMOJI.ROCK, style=ButtonStyle.gray)
#         self.playerchoice = playerchoice

#     async def callback(self, interaction: discord.Interaction):
#         if interaction.user not in self.playerchoice.rock:
#             self.playerchoice.rock.add(interaction.user)
#             game_instance  = RPSGame()
#             user_choice = "rock"
#             winner, bot_choice = game_instance.run(user_choice)

#             if winner is None:
#                 message = "It's a draw! Both chose: %s" % user_choice
#             elif winner is True:
#                 message = "You win: %s vs %s" % (user_choice, bot_choice)
#             elif winner is False:
#                 message = "You lose: %s vs %s" % (user_choice, bot_choice)
#             await interaction.response.send_message(message)


# class PaperButton(discord.ui.Button):
#     def __init__(self, playerchoice):
#         """Play Paper"""
#         super().__init__(emoji=EMOJI.PAPER, style=ButtonStyle.gray)
#         self.playerchoice = playerchoice

#     async def callback(self, interaction: discord.Interaction):
#         if interaction.user not in self.playerchoice.paper:
#             self.playerchoice.paper.add(interaction.user)
#             game_instance  = RPSGame()
#             user_choice = "paper"
#             winner, bot_choice = game_instance.run(user_choice)

#             if winner is None:
#                 message = "It's a draw! Both chose: %s" % user_choice
#             elif winner is True:
#                 message = "You win: %s vs %s" % (user_choice, bot_choice)
#             elif winner is False:
#                 message = "You lose: %s vs %s" % (user_choice, bot_choice)
#             await interaction.response.send_message(message)

# class ScissorButton(discord.ui.Button):
#     def __init__(self, playerchoice):
#         """Play Scissors"""
#         super().__init__(emoji=EMOJI.SCISSORS, style=ButtonStyle.gray)
#         self.playerchoice = playerchoice

#     async def callback(self, interaction: discord.Interaction):
#         if interaction.user not in self.playerchoice.scissors:
#             self.playerchoice.scissors.add(interaction.user)
#             game_instance  = RPSGame()
#             user_choice = "scissors"
#             winner, bot_choice = game_instance.run(user_choice)

#             if winner is None:
#                 message = "It's a draw! Both chose: %s" % user_choice
#             elif winner is True:
#                 message = "You win: %s vs %s" % (user_choice, bot_choice)
#             elif winner is False:
#                 message = "You lose: %s vs %s" % (user_choice, bot_choice)
#             await interaction.response.send_message(message)


# class RPS:
#     ROCK = "rock"
#     PAPER = "paper"
#     SCISSORS = "scissors"

#     def get_choices(self):
#         return(self.ROCK, self.PAPER, self.SCISSORS)
    
#     def check_win(self, choice1, choice2):
#         winner_check = {
#             (RPS.ROCK, RPS.PAPER): False,
#             (RPS.ROCK, RPS.SCISSORS): True,
#             (RPS.PAPER, RPS.ROCK): True,
#             (RPS.PAPER, RPS.SCISSORS): False,
#             (RPS.SCISSORS, RPS.ROCK): False,
#             (RPS.SCISSORS, RPS.PAPER): True,
#         }

#         winner = None
#         if choice1 == choice2:
#             winner = None
#         else:
#             winner = winner_check[(choice1, choice2)]

#         return winner      

# class RPSGame():
#     def run(self, user_choice):
#         rps_instance = RPS()

#         bot_choice = rand.choice(rps_instance.get_choices())

#         winner = rps_instance.check_win(user_choice, bot_choice)

#         return winner, bot_choice


# class RPSClass:
#     def __init__(self):
#         self.rock = set()
#         self.paper = set()
#         self.scissors = set()

#     @property
#     def embed(self):
#          return discord.Embed(
#             title="Choose Rock, Paper or Scissors",
#             color=discord.Color.blue()
#          )

#     @property
#     def controller(self):
#         return discord.ui.View(RockButton(self), PaperButton(self), ScissorButton(self), timeout=60)

# class Rockpaperscissors(discord.Cog):
#     """Play Rock Paper Scissors"""

#     def __init__(self, bot):
#         self.bot = bot
#         self.playerchoice = {}

#     def get_choice(self, message):
#         return self.playerchoice.get(message.id)

#     @slash_command(name="rps", guild_ids=devguilds)
#     async def rps(self, ctx):
#         """Command to check if bot is alive or if you need a friend."""
#         choice = RPSClass()
#         message = await ctx.respond(embed=choice.embed, view=choice.controller)
#         self.playerchoice[message.id] = choice


# def setup(bot):
#     """Entry point for loading cogs. Required for all cogs"""
#     bot.add_cog(Rockpaperscissors(bot))
