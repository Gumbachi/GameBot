import discord

class Game:
    def __init__(self, p1: discord.Member, p2: discord.Member):
        self.p1 = p1
        self.p2 = p2
        self.board = [TicTacToeButton(i) for i in range(9)]


    @property
    def view(self):
        return discord.View(*self.board)


class TicTacToeButton(discord.ui.Button):
    def __init__(self, index):
        super().__init__(label=index, style=ButtonStyle.green)
        self.index = index



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
