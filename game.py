import os
from time import sleep

from pynput.keyboard import Listener, Key

from board import Board
from snake import Snake


direction = None


def on_press(key):
    global direction
    if key == Key.up:
        direction = 'UP'
    if key == Key.down:
        direction = 'DOWN'
    if key == Key.right:
        direction = 'RIGHT'
    if key == Key.left:
        direction = 'LEFT'


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

    def start(self):
        while True:
            self.timer += 1
            if self.timer % self.snake_speed == 0:
                self.snake.set_dir(direction)
                self.snake.move()
                self.board.update(self.snake)

            clear_console()
            self.board.print()
            sleep(self.delay)
