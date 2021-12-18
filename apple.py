from random import randint, choice, seed
from board import EMPTY, APPLE

from board import colours


class Apple:

    def __init__(self, board):
        self.x = None
        self.y = None
        self.colour = None
        self.create(board)

    def create(self, board):
        pos_x, pos_y = None, None
        created = False
        while not created:
            pos_x = randint(1, board.rows - 2)
            pos_y = randint(1, board.cols - 2)
            if board.board[pos_x][pos_y] == EMPTY:
                board.board[pos_x][pos_y] = APPLE
                created = True
        self.x, self.y = pos_x, pos_y
        seed()
        self.colour = choice(list(colours.values()))
