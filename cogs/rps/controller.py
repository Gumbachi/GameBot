import random as rand
from .model import RPS

class RPSGame():
    def run(self, user_choice):
        rps_instance = RPS()

        bot_choice = rand.choice(rps_instance.get_choices())

        winner = rps_instance.check_win(user_choice, bot_choice)

        return winner, bot_choice