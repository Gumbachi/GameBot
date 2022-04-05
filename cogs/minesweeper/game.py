import random
import discord
from discord.enums import ButtonStyle
from discord.ui import View, Button

from .components import *


class Game:
    def __init__(self, size=9, mines=10):
        self.width = size
        self.height = size
        self.grid = [[' ' for _ in range(self.width)]
                     for _ in range(self.height)]
        self.mines = []
        self.flags = []
        self.placing_flag = False
        self.placemines(mines)

    def __str__(self):
        line = "|-----------------------------------|\n"
        string = "| A | B | C | D | E | F | G | H | I |\n"
        for i in range(self.width):
            string += line
            for j in range(self.height):
                string += f"| {self.grid[i][j]} "

            string += f"| {i + 1}\n"

        string += line
        return string

    @ property
    def view(self):
        return View(
            NextButton(self),
            FlagButton(self)
        )

    def getrandomcell(self):
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        return (y, x)

    def placemines(self, mines):
        for _ in range(mines):
            cell = self.getrandomcell()
            while cell in self.mines:
                cell = self.getrandomcell()
            self.mines.append(cell)

    def get_neighbors(self, row, col) -> list[tuple]:
        """Produces a list of neighbors as coordinate tuples"""
        poschanges = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        neighbors = []

        for poschange in poschanges:
            neighbor = (row + poschange[0], col + poschange[1])

            # check if in bounds
            if not (0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height):
                continue

            neighbors.append(neighbor)

        return neighbors

    def placeflag(self, cell):
        self.flags.append(cell)
        self.grid[cell[0]][cell[1]] = "F"
        self.placing_flag = False

    def detonate_location(self, cell):
        print(f"Detonating at {cell}")
        if cell in self.mines:
            print("YOU LOST")
            self.reveal_mines()
        else:
            self.reveal_surrounding(cell)

    def reveal_surrounding(self, cell):
        """Absolutely wicked recursion method."""

        if self.grid[cell[0]][cell[1]] != " ":
            return

        self.grid[cell[0]][cell[1]] = str(self.count_mines(cell))
        if self.count_mines(cell) != 0:
            return

        for n in self.get_neighbors(*cell):
            self.reveal_surrounding(n)

    def count_mines(self, cell):
        neighbors = self.get_neighbors(*cell)
        count = 0
        for n in neighbors:
            if n in self.mines:
                count += 1

        return count

    def reveal_mines(self):
        for mine in self.mines:
            self.grid[mine[0]][mine[1]] = 'X'

    def parse_input(self, input):
        letter_map = {l: n for l, n in zip("ABCDEFGHI", range(0, 9))}

        x, y = list(input)

        return (int(y) - 1, letter_map[x.upper()])

    def cellvalue(self, cell):
        neighbors = self.get_neighbors(*cell)

        count = 0
        for n in neighbors:
            if n in self.mines:
                count += 1
        return count
