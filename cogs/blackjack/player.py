import discord

from cogs.blackjack.constants import VALUES


class Player():
    def __init__(self, user: discord.Member = None):

        self.user = user
        self.id = self.user.id
        self.cards: list[str] = []  # The users cards
        self.playable = True
        self.win = False

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

        # put aces at the back for calculation
        self.cards.sort(key='A'.__eq__)

        total = 0
        for card in self.cards:
            cardface = card[:-1]  # Cut out the suit

            if cardface == 'A':
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
            else:
                total += VALUES[cardface]
        return total

    @property
    def hand(self):
        """Displays the hand of the player"""
        return "\n".join(self.cards)

    @property
    def locked(self):
        return "🔓" if self.playable else "🔒"

    @property
    def busted(self):
        return self.total > 21
