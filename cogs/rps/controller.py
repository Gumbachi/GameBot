# import random
# from .model import RPS

# class RPSGame:
#     def run(self, user_choice):
#         rps_instance = RPS()

#         if user_choice not in rps_instance.get_choices():
#             raise Exception("Invalid Choice: %s is not a valid choice" % user_choice)

#         bot_choice = random.choice(rps_instance.get_choices())

#         winner = rps_instance.check_win(user_choice, bot_choice)

#         return winner, bot_choice