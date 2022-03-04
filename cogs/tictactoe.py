import discord
from common.cfg import devguilds
from discord.commands import slash_command
from discord import ButtonStyle, Embed
from common.cfg import Emoji
from typing import List

class TicTacToeButton(discord.ui.Button):
    def __init__(self):
        super().__init__(style=ButtonStyle.green)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return
        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = "X"
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = "O"
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"
        self.disabled = True
        winner = view.winStatus()
        if winner is not None:
            if winner == view.X:
                content = "X wins."
            elif winner == view.O:
                content = "O wins."
            else:
                content = "It's a tie."

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)

class TicTacToe(discord.Cog):
    # players
    # board = [[]]
    children: List[TicTacToeButton]
    O = -1
    X = 1
    draw = 2
    def __init__(self, bot):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for i in range(3):
            for j in range(3):
                self.add_item(TicTacToeButton)

    def winStatus(self):
        # horizontal win
        for i in self.board:
            score = sum(i)
            if score == -3:
                return self.X
            elif score == 3:
                return self.O
        # vertical win
        for i in range(3):
            score = self.board[0][i] + self.board[1][i] + self.board[2][i]
            if score == -3:
                return self.X
            elif score == 3:
                return self.O
        # diagonal win
        # top left -> bottom right diagonal
        diagonal = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diagonal == -3:
            return self.X
        elif diagonal == 3:
            return self.O

        # top right -> bottom left diagonal
        diagonal = self.board[2][0] + self[1][1] + self[0][2]
        if diagonal == -3:
            return self.X
        elif diagonal == 3:
            return self.O

        return None

    @slash_command(name="tictactoe", guild_id=devguilds)
    async def ttt(self, ctx):
        return

def setup(bot):
    bot.add_cog(TicTacToe(bot))




