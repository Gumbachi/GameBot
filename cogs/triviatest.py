import unittest
from unittest import TestCase
import trivia
from trivia.game import Game


class TestTrueQuestions(TestCase):
    def test_right_answer_true(self):
        game = Game()
        game.question = game.qa[0]
        self.assertTrue(game.question_is_true())

    def test_wrong_answer_false(self):
        game = Game()
        game.question = game.qa[1]
        self.assertFalse(game.question_is_true())


class TestFalseQuestions(TestCase):
    def test_right_answer_false(self):
        game = Game()
        game.question = game.qa[3]
        self.assertTrue(game.question_is_false())

    def test_wrong_answer_true(self):
        game = Game()
        game.question = game.qa[5]
        self.assertFalse(game.question_is_false())


if __name__ == '__main__':
    unittest.main()
