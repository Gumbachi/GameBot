import discord
import random

from cogs.blackjack.components import BlackjackView
from cogs.blackjack.player import Player
from cogs.blackjack.constants import *
from common.cfg import bot


class Game:
    """Game object to facilitate game state and game actions."""

    def __init__(self, members: list[discord.Member]):
        self.dealer = Player(bot.user)
        self.players = [Player(member) for member in members]
        # Populate deck (52 cards)
        self.deck = [f"{c}{s}" for c in CARDS for s in SUITS]

        # Shuffle and deal cards
        random.shuffle(self.deck)
        self.deal_initial_cards()

        self._playerindex = 0

    @property
    def turn(self):
        return self.players[self._playerindex]

    @property
    def embed(self):
        """Formats the game into a discord Embed."""

        embed = discord.Embed(title="Blackjack", color=discord.Color.blue())
        embed.add_field(
            name=f"{self.dealer.name} ({self.dealer.total})",
            value=self.dealer.hand,
            inline=False
        )

        for player in self.players:
            turn = "⭐" if player == self.turn else ""

            embed.add_field(
                name=f"{turn} {player.name} ({player.total}) {player.locked}",
                value=player.hand
            )

        return embed

    @property
    def view(self) -> discord.ui.View:
        return BlackjackView(self)

    def deal_cards(self, player: Player, amount: int = 1):
        """Remove card(s) from the deck and add to a players hand"""
        for _ in range(amount):
            player.cards.append(self.deck.pop(0))

    def deal_initial_cards(self):
        """Deals 2 cards for each player and dealer."""
        self.deal_cards(self.dealer, 2)
        for player in self.players:
            self.deal_cards(player, 2)

    def cycle_to_next_player(self):
        """Moves the player index up or cycles it around"""
        if self._playerindex + 1 == len(self.players):
            self._playerindex = 0
        else:
            self._playerindex += 1