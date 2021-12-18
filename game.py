import os
from time import sleep

from board import Board
from snake import Snake


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


class Game:

    def __init__(self, fps, x, y, snake_speed, snake_length):
        clear_console()
        print('SNAKE loading...')
        self.delay = 1/fps
        self.board = Board(50, 50)
        self.snake = Snake(snake_length, int(x/2), int(y/2))
        self.timer = 0
        self.snake_speed = snake_speed
        sleep(1)

    def on_press(key):
        pass

    def start(self):

        while True:
            self.timer += 1
            if self.timer % self.snake_speed == 0:
                self.snake.move()
                self.board.update(self.snake)

            clear_console()
            self.board.print()
            sleep(self.delay)
