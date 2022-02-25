import random
from types import NoneType

class Parser:
    def __init__(self, choice):
        choice = choice.lower()

        if choice == RPS.ROCK:
            self.choice = RPS.ROCK
        elif choice == RPS.PAPER:
            self.choice = RPS.PAPER
        elif choice == RPS.SCISSORS:
            self.choice = RPS.SCISSORS
        else:
            raise


class RPSGame:
    def run(self, user_choice):
        rps_instance = RPS()

        if user_choice not in rps_instance.get_choices():
            raise Exception("Invalid Choice: %s is not a valid choice" % user_choice)

        bot_choice = random.choice(rps_instance.get_choices())

        winner = rps_instance.check_win(user_choice, bot_choice)

        return winner, bot_choice

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

