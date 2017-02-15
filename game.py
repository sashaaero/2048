# 2048 game
# Note: This game ends when you reach the 2048 number (Not infinite as usuall)
from PyQt5.QtCore import Qt
import random


class Game:
    size = 4 # field's size
    sym_len = 4 # for debug printing field
    field = [([None] * 4) for _ in range(size)] # field init
    up, right, down, left = range(4)
    actions = {
        Qt.Key_Left: left,
        Qt.Key_Right: right,
        Qt.Key_Down: down,
        Qt.Key_Up: up
    } # we're using keyboard's arrows
    over = False # flag that shows that game is finished (maybe rename to win?)

    def __init__(self):
        # we create two numbers as start
        self.create()
        self.create()

    @staticmethod
    def get_random_num():
        # returns 2 with 90% chance and 4 with other 10
        l = [2] * 9
        l.append(4)
        return random.choice(l)

    def get_random_empty_cell(self):
        # for setting place for new number
        l = []
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] is None:
                    l.append((i, j))
        return random.choice(l)

    def create(self, val=None):
        # add single new number in field
        # arg val is dev arg that can add a number you want
        i, j = self.get_random_empty_cell()
        val = self.get_random_num() if val is None else val
        self.field[i][j] = val

    def print_field(self):
        # dev method for priting field
        for row in self.field:
            for cell in row:
                print((str(cell) if cell is not None else '0').ljust(self.sym_len), end='')
            print()

    def move(self, action):
        # main action for game
        # algo: we move and plus 1 by one
        # so line 8 4 2 2 will go to 0 0 0 16 by single move
        if self.over: return
        old_field = [[cell for cell in row] for row in self.field] # after move we check if nothing changed
        #                                                            so there is no need to create new number
        direction = self.actions[action]

        if direction == self.up:
            for row in range(1, self.size):
                for col in range(self.size):
                    if self.field[row][col] is None:
                        continue

                    new_row = row - 1
                    while new_row >= 0 and self.field[new_row][col] is None:
                        new_row -= 1

                    if new_row == -1:
                        self.field[0][col] = self.field[row][col]
                        self.field[row][col] = None
                    elif self.field[new_row][col] == self.field[row][col]:
                        self.field[new_row][col] *= 2
                        self.field[row][col] = None
                    else:
                        val = self.field[row][col]
                        self.field[row][col] = None
                        self.field[new_row + 1][col] = val

        elif direction == self.right:
            for col in reversed(range(self.size - 1)):
                for row in range(self.size):
                    if self.field[row][col] is None:
                        continue

                    new_col = col + 1
                    while new_col < self.size and self.field[row][new_col] is None:
                        new_col += 1

                    if new_col == self.size:
                        self.field[row][self.size - 1] = self.field[row][col]
                        self.field[row][col] = None
                    elif self.field[row][new_col] == self.field[row][col]:
                        self.field[row][new_col] *= 2
                        self.field[row][col] = None
                    else:
                        val = self.field[row][col]
                        self.field[row][col] = None
                        self.field[row][new_col - 1] = val

        elif direction == self.down:
            for row in reversed(range(self.size - 1)):
                for col in range(self.size):
                    if self.field[row][col] is None:
                        continue

                    new_row = row + 1
                    while new_row < self.size and self.field[new_row][col] is None:
                        new_row += 1

                    if new_row == self.size:
                        self.field[self.size - 1][col] = self.field[row][col]
                        self.field[row][col] = None
                    elif self.field[new_row][col] == self.field[row][col]:
                        self.field[new_row][col] *= 2
                        self.field[row][col] = None
                    else:
                        val = self.field[row][col]
                        self.field[row][col] = None
                        self.field[new_row - 1][col] = val

        elif direction == self.left:
            for col in range(1, self.size):
                for row in range(self.size):
                    if self.field[row][col] is None:
                        continue

                    new_col = col - 1
                    while new_col >= 0 and self.field[row][new_col] is None:
                        new_col -= 1

                    if new_col == -1:
                        self.field[row][new_col + 1] = self.field[row][col]
                        self.field[row][col] = None
                    elif self.field[row][new_col] == self.field[row][col]:
                        self.field[row][new_col] *= 2
                        self.field[row][col] = None
                    else:
                        val = self.field[row][col]
                        self.field[row][col] = None
                        self.field[row][new_col + 1] = val

        if self.field != old_field:
            self.create()

        for row in self.field:
            for cell in row:
                if cell == 2048:
                    self.over = True
                    break
