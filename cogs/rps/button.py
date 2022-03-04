import discord
from discord.enums import ButtonStyle
from .controller import RPSGame
from common.cfg import EMOJI
from discord.ui import View 
from discord.ui import Button
from database import HallBotDB, Attribute

# Initializes the Database & creates a table
test_db = HallBotDB("Test")
test_db.create_table("Players", ["Name", "RPS Wins"])

class RockButton(discord.ui.Button):
    def __init__(self, playerchoice):
        """Play Rock"""
        super().__init__(emoji=EMOJI.ROCK, style=ButtonStyle.gray)
        self.playerchoice = playerchoice

    async def callback(self, interaction: discord.Interaction):
        if interaction.user not in self.playerchoice.rock:
            self.playerchoice.rock.add(interaction.user)
            game_instance = RPSGame()
            user_choice = "rock"
            winner, bot_choice = game_instance.run(user_choice)

            if winner is None:
                message = "It's a draw! Both chose: %s" % user_choice
            elif winner is True:
                message = "You win: %s vs %s" % (user_choice, bot_choice)
                # Adds 1 Win into the database for every win
                test_db.get_table("Players").add_attribute(Attribute([f"{interaction.user}", 1], False))
                for table in test_db.database:
                    print(f"Table: {table.name}")
                    for attribute in table.attributes:
                        print(f"Attribute: {attribute.values}")
            elif winner is False:
                message = "You lose: %s vs %s" % (user_choice, bot_choice)
            await interaction.response.send_message(message)


class PaperButton(discord.ui.Button):
    def __init__(self, playerchoice):
        """Play Paper"""
        super().__init__(emoji=EMOJI.PAPER, style=ButtonStyle.gray)
        self.playerchoice = playerchoice

    async def callback(self, interaction: discord.Interaction):
        if interaction.user not in self.playerchoice.paper:
            self.playerchoice.paper.add(interaction.user)
            game_instance = RPSGame()
            user_choice = "paper"
            winner, bot_choice = game_instance.run(user_choice)

            if winner is None:
                message = "It's a draw! Both chose: %s" % user_choice
            elif winner is True:
                message = "You win: %s vs %s" % (user_choice, bot_choice)
                test_db.get_table("Players").add_attribute(Attribute([f"{interaction.user}", 1], False))
                for table in test_db.database:
                    print(f"Table: {table.name}")
                    for attribute in table.attributes:
                        print(f"Attribute: {attribute.values}")
            elif winner is False:
                message = "You lose: %s vs %s" % (user_choice, bot_choice)
            await interaction.response.send_message(message)

class ScissorButton(discord.ui.Button):
    def __init__(self, playerchoice):
        """Play Scissors"""
        super().__init__(emoji=EMOJI.SCISSORS, style=ButtonStyle.gray)
        self.playerchoice = playerchoice

    async def callback(self, interaction: discord.Interaction):
        if interaction.user not in self.playerchoice.scissors:
            self.playerchoice.scissors.add(interaction.user)
            game_instance = RPSGame()
            user_choice = "scissors"
            winner, bot_choice = game_instance.run(user_choice)

            if winner is None:
                message = "It's a draw! Both chose: %s" % user_choice
            elif winner is True:
                message = "You win: %s vs %s" % (user_choice, bot_choice)
                test_db.get_table("Players").add_attribute(Attribute([f"{interaction.user}", 1], False))
                for table in test_db.database:
                    print(f"Table: {table.name}")
                    for attribute in table.attributes:
                        print(f"Attribute: {attribute.values}")
            elif winner is False:
                message = "You lose: %s vs %s" % (user_choice, bot_choice)
            await interaction.response.send_message(message)
