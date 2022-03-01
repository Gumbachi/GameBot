class RPS:
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    def get_choices(self):
        return(self.ROCK, self.PAPER, self.SCISSORS)
    
    def check_win(self, choice1, choice2):
        winner_check = {
            (RPS.ROCK, RPS.PAPER): False,
            (RPS.ROCK, RPS.SCISSORS): True,
            (RPS.PAPER, RPS.ROCK): True,
            (RPS.PAPER, RPS.SCISSORS): False,
            (RPS.SCISSORS, RPS.ROCK): False,
            (RPS.SCISSORS, RPS.PAPER): True,
        }

        winner = None
        if choice1 == choice2:
            winner = None
        else:
            winner = winner_check[(choice1, choice2)]

        return winner