import discord
from common.cfg import devguilds
from discord.commands import slash_command
from .game import Game


class TicTacToe(discord.Cog):
    instances = {}

    O = -1
    X = 1
    draw = 2

    def __init__(self, bot):
        self.bot = bot
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        # for i in range(3):
        # for j in range(3):
        # self.add_item(TicTacToeButton)

    @slash_command(name="tictactoe", guild_ids=devguilds)
    async def startGame(self, ctx, opponent: discord.Member):
        game = Game(ctx.author, opponent)
        self.instances[ctx.guild.id] = game
        await ctx.respond(f"{ctx.author} vs {opponent}", view=game.view)

    # def winStatus(self):
    #     # horizontal win
    #     for i in self.board:
    #         score = sum(i)
    #         if score == -3:
    #             return self.X
    #         elif score == 3:
    #             return self.O
    #     # vertical win
    #     for i in range(3):
    #         score = self.board[0][i] + self.board[1][i] + self.board[2][i]
    #         if score == -3:
    #             return self.X
    #         elif score == 3:
    #             return self.O
    #     # diagonal win
    #     # top left -> bottom right diagonal
    #     diagonal = self.board[0][0] + self.board[1][1] + self.board[2][2]
    #     if diagonal == -3:
    #         return self.X
    #     elif diagonal == 3:
    #         return self.O
    #
    #     # top right -> bottom left diagonal
    #     diagonal = self.board[2][0] + self[1][1] + self[0][2]
    #     if diagonal == -3:
    #         return self.X
    #     elif diagonal == 3:
    #         return self.O
    #
    #     if all(i != 0 for row in self.board for i in row):
    #         return self.Tie
    #     return None


def setup(bot):
    bot.add_cog(TicTacToe(bot))
