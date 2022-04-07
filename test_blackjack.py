import unittest
from cogs.blackjack.game import Game
from cogs.blackjack.player import Player


class BlackjackTests(unittest.TestCase):

    def test_populate_deck(self):
        game = Game(["Dummy Player"])
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
        player = Player("dummy")

        # Testing with Ace
        player.hand = ['A♠', '7♥']
        expected = 18
        actual = player.total
        self.assertEqual(expected, actual)

        # Testing with 10 and face card
        player.hand = ['K♠', '10♥']
        expected = 20
        actual = player.total
        self.assertEqual(expected, actual)
