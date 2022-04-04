import discord
import random
import re

class Game:
    def __init__(self):
        self.word_list = [
            "hangman",
            "hello",
            "test",
            "computer",
            "science",
            "champlain"
        ]
        self.tries = 6
        self.guessed_letters = []
        self.word = self.word_list[random.randint(0, len(self.word_list)-1)]
        print(self.word)
        self.progress = "-" * len(self.word)

    def set_word(self, word):
        self.word = word

    def set_progress(self, progress):
        self.progress = progress

    def set_tries(self, tries):
        self.tries = tries

    def check_win(self):
        if self.word == self.progress and self.word != "":
            return True
        return False

    def check_loss(self):
        if self.tries <= 0:
            return True
        return False

    def guess_letter(self, guess):
        #if guess not in self.guessed_letters:
        self.guessed_letters.append(guess)
        if guess in self.word and self.tries > 0:
            self.progress = "".join(
                ["-" if c not in self.guessed_letters else guess for c in self.word])
            return True
        else:
            self.tries -= 1
            return False
