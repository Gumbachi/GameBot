import discord
import random

from cogs.blackjack.components import BlackjackView
from cogs.blackjack.player import Player
from cogs.blackjack.constants import *
from common.cfg import bot


class Game:
    """Game object to facilitate game state and game actions."""

    def __init__(self, members: list[discord.Member]):
        self.headline = "Blackjack"
        self.isfinished = False
        self.dealer = Player()

        print("DEALER CREATED")

        self.dealer.win = True  # Dealer wins by default and changed if player wins
        self.players = [Player(member) for member in members]
        # Populate deck (52 cards)
        self.deck = [f"{c}{s}" for c in CARDS for s in SUITS]

        # Shuffle and deal cards
        random.shuffle(self.deck)
        self.deal_initial_cards()

    @property
    def embed(self):
        """Formats the game into a discord Embed."""

        embed = discord.Embed(title=self.headline, color=discord.Color.blue())

        if self.isfinished:
            dealer_total = self.dealer.total
            dealer_hand = self.dealer.hand
        else:
            dealer_total = "??"
            dealer_hand = f"{self.dealer.cards[0]}\n??"

        embed.add_field(
            name=f"{self.dealer.name} ({dealer_total})",
            value=dealer_hand,
            inline=False
        )

        for player in self.players:
            embed.add_field(
                name=f"{player.name} ({player.total}) {player.locked}",
                value=player.hand
            )

        return embed

    @property
    def view(self) -> discord.ui.View:
        return BlackjackView(self)

    def find_player_by_id(self, id: int):
        """Find a player based on their id."""
        for player in self.players:
            if player.id == id:
                return player

    def deal_cards(self, player: Player, amount: int = 1):
        """Remove card(s) from the deck and add to a players hand"""
        for _ in range(amount):
            player.cards.append(self.deck.pop(0))

    def deal_initial_cards(self):
        """Deals 2 cards for each player and dealer."""
        self.deal_cards(player=self.dealer, amount=2)
        for player in self.players:
            self.deal_cards(player=player, amount=2)

    def all_locked_in(self):
        """Check if all players are finished drawing."""
        return all([not p.playable for p in self.players])

    def play_dealer(self):
        """Plays out the rest of the dealers hand."""
        while self.dealer.total < 17:
            self.deal_cards(player=self.dealer, amount=1)

    def play_dealer(self):
        """Plays out the rest of the dealers hand."""
        while self.dealer.total < 17:
            self.deal_cards(player=self.dealer, amount=1)

    def determine_winner(self):
        """Determine who won the game."""

        if self.dealer.busted:
            self.dealer.win = False

        for player in self.players:

            if player.busted:
                continue

            elif not player.busted and self.dealer.busted:
                player.win = True

            elif player.total > self.dealer.total:
                player.win = True
                self.dealer.win = False

        # Dealer wins
        if self.dealer.win:
            self.headline = "Dealer Wins"

        # Tie game
        elif all([not player.win for player in self.players]) and not self.dealer.win:
            self.headline = "It's a tie / push whatever :)"

        # Player wins
        else:
            self.headline = f"{', '.join(p.name for p in self.players if p.win)} Wins"

        self.isfinished = True
