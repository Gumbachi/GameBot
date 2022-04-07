import discord
from discord import slash_command, Option
from cogs.blackjack.game import Game
from common.cfg import devguilds


class Blackjack(discord.Cog):
    """Blackjack commands and listeners."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="blackjack", guild_ids=devguilds)
    async def start_blackjack(
        self, ctx: discord.ApplicationContext,
        player2: Option(discord.Member, "Player 2", default=None),
        player3: Option(discord.Member, "Player 3", default=None),
        player4: Option(discord.Member, "Player 4", default=None),
        player5: Option(discord.Member, "Player 5", default=None),
        player6: Option(discord.Member, "Player 6", default=None),
        player7: Option(discord.Member, "Player 7", default=None)
    ):
        """Begin a game of Connect Four with a friend."""

        players = [
            ctx.author, player2, player3,
            player4, player5, player6, player7
        ]
        # filter out None
        players = [player for player in players if player]

        print(f"STARTING GAME WITH {players}")

        game = Game(players)
        await ctx.respond(embed=game.embed, view=game.view)


def setup(bot):
    """Entry point for loading cogs. Required for all cogs"""
    bot.add_cog(Blackjack(bot))
