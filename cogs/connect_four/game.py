import discord


class Emoji:
    RED = "🔴"
    BLACK = "⚫"
    YELLOW = "🟡"


class Game:
    """Game object to facilitate game state and game actions."""

    def __init__(self, playerone: discord.Member, playertwo: discord.Member):
        self.playerone = playerone
        self.playertwo = playertwo
        self.board = [[Emoji.BLACK] * 7 for _ in range(6)]

    def __str__(self):
        string = ""
        for row in self.board:
            string += "|".join(row) + "\n"

        return string

    @property
    def embed(self) -> discord.Embed:
        """Formats the game into a discord Embed."""
        return discord.Embed(
            title=f"{self.playerone.name} VS {self.playertwo.name}",
            description=str(self),
            color=discord.Color.blurple()
        )
