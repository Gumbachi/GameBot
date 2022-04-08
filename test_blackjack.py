import unittest
from unittest.mock import MagicMock


from cogs.blackjack.game import Game
from cogs.blackjack.player import Player

from discord import Member


class DummyUser:
    def __init__(self):
        self.id = 1
        self.bot = False


class BlackjackTests(unittest.TestCase):

    def test_populate_deck(self):
        game = Game([DummyUser()])
        expected = [
            'A♠', 'A♥', 'A♣', 'A♦', '2♠', '2♥', '2♣', '2♦',
            '3♠', '3♥', '3♣', '3♦', '4♠', '4♥', '4♣', '4♦',
            '5♠', '5♥', '5♣', '5♦', '6♠', '6♥', '6♣', '6♦',
            '7♠', '7♥', '7♣', '7♦', '8♠', '8♥', '8♣', '8♦',
            '9♠', '9♥', '9♣', '9♦', '10♠', '10♥', '10♣', '10♦',
            'J♠', 'J♥', 'J♣', 'J♦', 'Q♠', 'Q♥', 'Q♣', 'Q♦', 'K♠', 'K♥', 'K♣', 'K♦'
        ]
        self.assertCountEqual(expected, game.deck)

    def test_calculate_total(self):
        player = Player(DummyUser())

        # Testing with Ace
        player.cards = ['A♠', '7♥']
        expected = 18
        actual = player.total
        self.assertEqual(expected, actual)

        # Testing with 10 and face card
        player.cards = ['K♠', '10♥']
        expected = 20
        actual = player.total
        self.assertEqual(expected, actual)

        # Testing with Aces
        player.cards = ['A♠', 'A♥', 'A♣', '10♣']
        expected = 13
        actual = player.total
        self.assertEqual(expected, actual)

        # More Ace testing
        player.cards = ['A♠', 'A♥', '6♣']
        expected = 18
        actual = player.total
        self.assertEqual(expected, actual)
