import discord

# This is here for typing to avoid cyclic import
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cogs.blackjack.game import Game


class BlackjackView(discord.ui.View):
    def __init__(self, game: 'Game'):
        super().__init__(
            HitButton(game),
            StandButton(game),
            timeout=300
        )

    async def on_timeout(self):
        pass


class StandButton(discord.ui.Button):
    def __init__(self, game: 'Game'):
        super().__init__(label="STAND")
        self.game = game

    async def callback(self, interaction: discord.Interaction):

        player = self.game.turn

        # if interaction.user != self.game.turn:
        #     return

        player.playable = False  # disable player from playing

        self.game.cycle_to_next_player()
        await interaction.response.edit_message(embed=self.game.embed)


class HitButton(discord.ui.Button):
    def __init__(self, game: 'Game'):
        super().__init__(label="HIT")
        self.game = game

    async def callback(self, interaction: discord.Interaction):

        player = self.game.turn

        if not player.playable:
            return

        self.game.deal_cards(player)

        self.game.cycle_to_next_player()

        await interaction.response.edit_message(embed=self.game.embed)
