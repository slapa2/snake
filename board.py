import random
from colours import colours


EMPTY = '  '
TOP_CORNER = '_'
BOTTOM_CORNER = '|'
SIDE = '|'
TOP = '__'
BOTTOM = '__'
SNAKE = f'{colours["G"]}██{colours["W"]}'
APPLE = '██'


class Board:

    def __init__(self, rows, cols):
        random.seed()
        self.rows = rows
        self.cols = cols

        self.board = [[EMPTY for _ in range(cols)] for _ in range(rows)]

    def _clear(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0:
                    if j == 0 or j == self.cols - 1:
                        self.board[i][j] = TOP_CORNER
                    else:
                        self.board[i][j] = TOP
                elif i == self.rows - 1:
                    if j == 0 or j == self.cols - 1:
                        self.board[i][j] = BOTTOM_CORNER
                    else:
                        self.board[i][j] = BOTTOM
                else:
                    if j == 0 or j == self.cols - 1:
                        self.board[i][j] = SIDE
                        self.board[i][j] = SIDE
                    else:
                        self.board[i][j] = EMPTY
                        self.board[i][j] = EMPTY

    def update(self, snake, apple):
        self._clear()
        self.board[apple.x][apple.y] = f'{apple.colour}{APPLE}{colours["W"]}'
        for module in snake.body:
            self.board[module[1]][module[0]] = SNAKE

