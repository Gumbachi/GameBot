# import discord
# from discord.enums import ButtonStyle
# # from cogs.rps.rps import RPS
# from common.cfg import EMOJI
# from discord.ui import View 
# from discord.ui import Button

# class RockButton(Button):
#     def __init__(self):
#         """Play Rock"""
#         super().__init__(emoji=EMOJI.ROCK, style=ButtonStyle.gray)

#     async def callback(self, interaction: discord.Interaction):
#         await interaction.response.send_message("You Picked Rock")

# class PaperButton(Button):
#     def __init__(self):
#         """Play Paper"""
#         super().__init__(emoji=EMOJI.PAPER, style=ButtonStyle.gray)

#     async def callback(self, interaction: discord.Interaction):
#         await interaction.response.send_message("You Picked Paper")

# class ScissorButton(Button):
#     def __init__(self):
#         """Play Scissors"""
#         super().__init__(emoji=EMOJI.SCISSORS, style=ButtonStyle.gray)

#     async def callback(self, interaction: discord.Interaction):
#         await interaction.response.send_message("You Picked Scissors")

# def create_view(view: discord.ui.View = None):
#     """Creates the rps game view"""

#     if not view:
#         return View(RockButton(), PaperButton(), ScissorButton(), timeout=60)
