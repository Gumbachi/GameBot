import discord
from discord import ButtonStyle, Embed
from discord.ui import View, Button
import random


class Game:
    def __init__(self):
        self.buttons = [TriviaButtonTrue(self), TriviaButtonFalse(self)]
        self.qa = [
            ["Computer Science and Innovation is a major at Champlain college.", True],
            ["The sky is orange.", False],
            ["Brian Hall is your professor.", True],
            ["There are 205 bones in the human body.", False],
            ["Marie Curie is the only person to win a Nobel Prize in two different sciences.", True],
            ["The capitol of Libya is Tripoli.", True],
            ["The national animal of Scotland is the unicorn.", True],
            ["The Mediterranean Sea is the biggest sea.", False],
            ["Tomatoes are vegetables.", False],
            ["Venus is the only planet in the solar system to rotate clockwise.", True]
        ]
        self.question = self.qa[random.randint(0, len(self.qa)-1)]

    @property
    def view(self):
        return View(*self.buttons)

    def question_is_true(self):
        if self.question[1] == True:
            return True
        return False

    def question_is_false(self):
        if self.question[1] == False:
            return True
        return False


class TriviaButtonTrue(discord.ui.Button):
    def __init__(self, game):
        super().__init__(label="True", style=ButtonStyle.green)
        self.game = game

    async def callback(self, interaction: discord.Interaction):
        for button in self.game.buttons:
            button.disabled = True

        if self.game.question[1] == True:
            await interaction.response.edit_message(view=self.game.view, content="You were correct, the answer was true.")
        else:
            await interaction.response.edit_message(view=self.game.view, content="You were incorrect, the answer was false.")


class TriviaButtonFalse(discord.ui.Button):
    def __init__(self, game):
        super().__init__(label="False", style=ButtonStyle.red)
        self.game = game

    async def callback(self, interaction: discord.Interaction):
        for button in self.game.buttons:
            button.disabled = True

        if self.game.question[1] == False:
            await interaction.response.edit_message(view=self.game.view, content="You were correct, the answer was false")
        else:
            await interaction.response.edit_message(view=self.game.view, content="You were incorrect, the answer was true.")


