import random

colours = {
    'W': '\033[0m',  # white (normal)
    'R': '\033[31m',  # red
    'G': '\033[32m',  # green
    'Y': '\033[33m',  # yellow
    # 'B': '\033[34m',  # blue
    'M': '\033[35m',  # magenta
    # 'C': '\033[36m',  # cyan
}

EMPTY = '  '
TOP_CORNER = '_'
BOTTOM_CORNER = '|'
SIDE = '|'
TOP = '__'
BOTTOM = '__'
SNAKE = f'{colours["G"]}██{colours["W"]}'
APPLE = '██'


def print_colours_bar():
    for key, colour in colours.items():
        print(f'{colour}██{colours["W"]}', end='')
    print()


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

        if (
                snake.body[0][0] == 0 or
                snake.body[0][0] == self.cols - 1 or
                snake.body[0][1] == 0 or
                snake.body[0][1] == self.rows - 1
        ):
            raise Exception

        self.board[apple.x][apple.y] = f'{apple.colour}{APPLE}{colours["W"]}'
        for module in snake.body:
            self.board[module[1]][module[0]] = SNAKE

    def render(self):
        render = ''
        for row in self.board:
            for i, col in enumerate(row):
                render += col
            render += '\n'
        return render
