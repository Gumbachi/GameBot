import discord

# This is here for typing to avoid cyclic import
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cogs.minesweeper.game import Game


class InputField(discord.ui.Modal):
    def __init__(self, game: 'Game'):
        super().__init__(title="Input Coordinate")
        self.game = game
        self.add_item(
            discord.ui.InputText(
                label="Grid Coordinate",
                placeholder="(a5, d8, b3)",
                max_length=2
            )
        )

    async def callback(self, interaction: discord.Interaction):
        coordinates = self.game.parse_input(self.children[0].value)

        if self.game.placing_flag:
            self.game.placeflag(coordinates)
        else:
            self.game.detonate_location(coordinates)
            pass

        await interaction.response.send_message(
            content=f"```{self.game}```", view=self.game.view)


class NextButton(discord.ui.Button):
    def __init__(self, game: 'Game'):
        super().__init__(emoji="💥")
        self.game = game

    async def callback(self, interaction: discord.Interaction):
        self.game.placing_flag = False
        await interaction.response.send_modal(InputField(self.game))


class FlagButton(discord.ui.Button):
    def __init__(self, game: 'Game'):
        super().__init__(emoji="🚩")
        self.game = game

    async def callback(self, interaction: discord.Interaction):
        self.game.placing_flag = True
        await interaction.response.send_modal(InputField(self.game))
