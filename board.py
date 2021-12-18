EMPTY = '  '
TOP_CORNER = '_'
BOTTOM_CORNER = '|'
SIDE = '|'
TOP = '__'
BOTTOM = '__'
SNAKE = '██'
APPLE = '██'

class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        field = {
            'type': '',
            'content': '  '
        }
        self.board = [[field.copy() for _ in range(cols)] for _ in range(rows)]

    def _clear(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0:
                    if j == 0 or j == self.cols - 1:
                        self.board[i][j] = {'type': 'border', 'content': TOP_CORNER}
                    else:
                        self.board[i][j] = {'type': 'border', 'content': TOP}
                elif i == self.rows - 1:
                    if j == 0 or j == self.cols - 1:
                        self.board[i][j] = {'type': 'border', 'content': BOTTOM_CORNER}
                    else:
                        self.board[i][j] = {'type': 'border', 'content': BOTTOM}
                else:
                    if j == 0 or j == self.cols - 1:
                        self.board[i][j] = {'type': 'border', 'content': SIDE}
                        self.board[i][j] = {'type': 'border', 'content': SIDE}
                    else:
                        self.board[i][j] = {'type': 'empty', 'content': EMPTY}
                        self.board[i][j] = {'type': 'empty', 'content': EMPTY}

    def update(self, snake):
        self._clear()

        if (
            snake.body[0][0] == 0 or
            snake.body[0][0] == self.cols - 1 or
            snake.body[0][1] == 0 or
            snake.body[0][1] == self.rows - 1
        ):
            raise Exception

        for module in snake.body:
            self.board[module[1]][module[0]]['content'] = SNAKE
            self.board[module[1]][module[0]]['type'] = snake

    def render(self):
        render = ''
        for row in self.board:
            for i, col in enumerate(row):
                render += col['content']
            render += '\n'
        return render

    def print(self):
        print(self.render())
