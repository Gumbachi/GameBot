import unittest
from unittest import TestCase
import hangman
from hangman.game import Game


class TestWinCondition(TestCase):
    def test_win(self):
        game = Game()
        game.set_word("hello")
        game.set_progress("hello")
        self.assertTrue(game.check_win())

    def test_not_yet_won(self):
        game = Game()
        game.set_word("brother")
        game.set_progress("b-othe-")
        self.assertFalse(game.check_win())

    def test_loss(self):
        game = Game()
        game.set_word("lose")
        game.set_progress("----")
        game.set_tries(0)
        self.assertTrue(game.check_loss())

    def test_not_yet_lost(self):
        game = Game()
        game.set_word("win")
        game.set_progress("---")
        game.set_tries(7)
        self.assertFalse(game.check_loss())

if __name__ == '__main__':
    unittest.main()