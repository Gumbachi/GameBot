import discord
from discord.enums import ButtonStyle
from discord.ui import View, Button


class Game:
    def __init__(self, p1: discord.Member, p2: discord.Member):
        self.p1 = p1
        self.p2 = p2
        self.board = [TicTacToeButton(i, self) for i in range(9)]
        self.turn = p1

    @property
    def label(self):
        return "O" if self.turn == self.p2 else "X"

    @property
    def view(self):
        return View(*self.board)

    def change_turn(self):
        if self.turn == self.p1:
            self.turn = self.p2
        else:
            self.turn = self.p1

    def checkWin(self):
        # check horizontal X
        if self.board[0].label == "X" and self.board[1].label == "X" and self.board[2].label == "X":
            return "X"
        elif self.board[3].label == "X" and self.board[4].label == "X" and self.board[5].label == "X":
            return "X"
        elif self.board[6].label == "X" and self.board[7].label == "X" and self.board[8].label == "X":
            return "X"
        # check horizontal O
        elif self.board[0].label == "O" and self.board[1].label == "O" and self.board[2].label == "O":
            return "O"
        elif self.board[3].label == "O" and self.board[4].label == "O" and self.board[5].label == "O":
            return "O"
        elif self.board[6].label == "O" and self.board[7].label == "O" and self.board[8].label == "O":
            return "O"
        # check vertical X
        elif self.board[0].label == "X" and self.board[4].label == "X" and self.board[6].label == "X":
            return "X"
        elif self.board[1].label == "X" and self.board[5].label == "X" and self.board[7].label == "X":
            return "X"
        elif self.board[2].label == "X" and self.board[6].label == "X" and self.board[8].label == "X":
            return "X"
        # check vertical O
        elif self.board[0].label == "O" and self.board[4].label == "O" and self.board[6].label == "O":
            return "O"
        elif self.board[1].label == "O" and self.board[5].label == "O" and self.board[7].label == "O":
            return "O"
        elif self.board[2].label == "O" and self.board[6].label == "O" and self.board[8].label == "O":
            return "O"
        # check diagonal X
        elif self.board[0].label == "X" and self.board[4].label == "X" and self.board[8].label == "X":
            return "X"
        elif self.board[2].label == "X" and self.board[4].label == "X" and self.board[6].label == "X":
            return "X"
        #check diagonal O
        elif self.board[0].label == "O" and self.board[4].label == "O" and self.board[8].label == "O":
            return "O"
        elif self.board[2].label == "O" and self.board[4].label == "O" and self.board[6].label == "O":
            return "O"
        else:
            return


class TicTacToeButton(discord.ui.Button):
    def __init__(self, index, game):
        super().__init__(label="-", style=ButtonStyle.green, row=index // 3)
        self.game = game
        self.index = index

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.game.turn:
            return
        self.disabled = True
        self.label = self.game.label

        if self.game.checkWin() == "O":
            print("O wins")
            await interaction.response.edit_message(content="O wins")
        if self.game.checkWin() == "X":
            await interaction.response.edit_message(content="X wins")
            print("X wins")

        self.game.change_turn()
        await interaction.response.edit_message(view=self.game.view)
