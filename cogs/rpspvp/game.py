import discord
import random
from discord import ButtonStyle, Embed
from common.cfg import Emoji, bot
from database import HallBotDB, Attribute

rpswins = HallBotDB("Test")
rpswins.create_table("Players", ["Name", "RPS Wins"])

class PVPGame():

    def __init__(self, p1: discord.Member, p2: discord.Member):
        self.p1 = p1
        self.p2 = p2
        self.p1choice = None
        self.p2choice = None if not p2 == bot.user else random.choice(
            ["Rock", "Paper", "Scissors"])
        self.buttons = [RockButton(self), PaperButton(
            self), ScissorButton(self)]

    @property
    def embed(self):
        return discord.Embed(
            title=self.status,
            color=discord.Color.blue()
        )

    @property
    def controller(self):
        return discord.ui.View(*self.buttons, timeout=60)

    @property
    def winner(self):
        return {
            ("Rock", "Paper"): self.p2,
            ("Rock", "Scissors"): self.p1,
            ("Paper", "Rock"): self.p1,
            ("Paper", "Scissors"): self.p2,
            ("Scissors", "Rock"): self.p2,
            ("Scissors", "Paper"): self.p1,
        }.get((self.p1choice, self.p2choice))

    @property
    def status(self):

        if not self.p1choice and not self.p2choice:
            return f"{self.p1.name} vs {self.p2.name}"

        if self.p1choice == self.p2choice:
            self.end()
            return f"Its a tie you both chose {self.p1choice}"

        if not self.winner:
            return f"{self.p1.name} vs {self.p2.name}"

        self.end()

        if self.winner == self.p1:
            rpswins.get_table("Players").add_attribute(Attribute([self.p1.name, 1], False))
            return f"{self.p1choice} beats {self.p2choice} - {self.p1.name} Wins!"

        rpswins.get_table("Players").add_attribute(Attribute([self.p2.name, 1], False))
        return f"{self.p2choice} beats {self.p1choice} - {self.p2.name} Wins!"

    def end(self):
        for button in self.buttons:
            button.disabled = True


class RockButton(discord.ui.Button):
    def __init__(self, game):
        """Play Rock"""
        super().__init__(emoji=Emoji.ROCK, style=ButtonStyle.gray)
        self.game = game

    async def callback(self, interaction: discord.Interaction):
        if interaction.user not in (self.game.p1, self.game.p2):
            return

        if interaction.user == self.game.p1:
            self.game.p1choice = "Rock"
        else:
            self.game.p2choice = "Rock"
        await interaction.response.edit_message(embed=self.game.embed, view=self.game.controller)


class PaperButton(discord.ui.Button):
    def __init__(self, game):
        """Play Paper"""
        super().__init__(emoji=Emoji.PAPER, style=ButtonStyle.gray)
        self.game = game

    async def callback(self, interaction: discord.Interaction):
        if interaction.user not in (self.game.p1, self.game.p2):
            return

        if interaction.user == self.game.p1:
            self.game.p1choice = "Paper"
        else:
            self.game.p2choice = "Paper"

        await interaction.response.edit_message(embed=self.game.embed, view=self.game.controller)


class ScissorButton(discord.ui.Button):
    def __init__(self, game):
        """Play Scissors"""
        super().__init__(emoji=Emoji.SCISSORS, style=ButtonStyle.gray)
        self.game = game

    async def callback(self, interaction: discord.Interaction):
        if interaction.user not in (self.game.p1, self.game.p2):
            return

        if interaction.user == self.game.p1:
            self.game.p1choice = "Scissors"
        else:
            self.game.p2choice = "Scissors"

        await interaction.response.edit_message(embed=self.game.embed, view=self.game.controller)
