import unittest
from cogs.minesweeper.game import Game


class MinesweeperTests(unittest.TestCase):

    def test_getneighbors(self):
        game = Game()

        # Interior
        neighbors = game.get_neighbors(1, 1)
        self.assertCountEqual(
            neighbors, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])

        # Edge
        neighbors = game.get_neighbors(0, 0)
        self.assertCountEqual(
            neighbors, [(0, 1), (1, 1), (1, 0)])

    def test_placemines(self):
        game = Game()  # mines are placed on init
        self.assertEqual(len(game.mines), 10)

        game = Game(mines=3)  # mines are placed on init
        self.assertEqual(len(game.mines), 3)

    def test_placeflag(self):
        game = Game()

        flag_location = (2, 5)
        game.placeflag(flag_location)

        self.assertListEqual(game.flags, [flag_location])
        self.assertEqual(game.grid[flag_location[0]][flag_location[1]], 'F')

    def test_cellvalue(self):
        game = Game(size=3, mines=0)
        game.mines = [(1, 1), (0, 1)]  # manually place mine

        expected = 2
        actual = game.cellvalue((0, 0))
        self.assertEqual(expected, actual)

        expected = 1
        actual = game.cellvalue((2, 0))
        self.assertEqual(expected, actual)

    def test_dig(self):
        game = Game(size=3, mines=0)
        game.mines = [(0, 0)]

        print(f"GRID = {game.grid}")

        game.detonate_location((2, 2))

        expected = [
            [" ", "1", "0"],
            ["1", "1", "0"],
            ["0", "0", "0"],
        ]

        self.assertEqual(expected, game.grid)

    def test_parse_input(self):
        game = Game()

        actual = game.parse_input("c5")
        expected = (4, 2)

        self.assertEqual(expected, actual)

        actual = game.parse_input("a1")
        expected = (0, 0)

        self.assertEqual(expected, actual)
