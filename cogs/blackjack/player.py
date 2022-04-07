import discord

from cogs.blackjack.constants import VALUES


class Player():
    def __init__(self, user: discord.Member):
        self.user = user
        self.id = self.user.id
        self.cards: list[str] = []  # The users cards
        self.playable = True

    def __eq__(self, other: discord.User):
        if not isinstance(other, (discord.User, Player)):
            print("INVALID COMPARE TYPE")
            return False
        return self.user.id == other.id

    @property
    def name(self):
        if self.user.bot:
            return "Dealer"
        return self.user.nick or self.user.name

    @property
    def total(self):
        total = 0
        for card in self.cards:
            cardface = card[:-1]  # Cut out the suit
            total += VALUES[cardface]
        return total

    @property
    def hand(self):
        """Displays the hand of the player"""
        return "\n".join(self.cards)

    @property
    def locked(self):
        return "🔓" if self.playable else "🔒"
