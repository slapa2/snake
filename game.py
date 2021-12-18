import os
from time import sleep

from pynput.keyboard import Key

from board import Board
from snake import Snake
from apple import Apple
from colours import print_colours_bar
from printer import Printer

direction = "UP"
blocked_keyboard = False


def on_press(key):
    global direction
    global blocked_keyboard

    if not blocked_keyboard:
        if key == Key.up and direction != 'DOWN':
            direction = 'UP'
        if key == Key.down and direction != 'UP':
            direction = 'DOWN'
        if key == Key.right and direction != 'LEFT':
            direction = 'RIGHT'
        if key == Key.left and direction != 'RIGHT':
            direction = 'LEFT'
        blocked_keyboard = True


class Game:

    def __init__(self, fps, x, y, snake_speed, snake_length):
        self.delay = 1/fps
        self.board = Board(x, y)
        self.snake = Snake(snake_length, int(x/2), int(y/2))
        self.timer = 0
        self.apple_counter = 1
        self.points = 0
        self.snake_speed = snake_speed
        self.apple = Apple(self.board)
        self.printer = Printer()
        # self.printer.print_all_numbers()
        for i in reversed(range(1, 4)):
            self.printer.clear_console()
            self.printer.print_logo()
            self.printer.print_number(i)
            sleep(1)


    def check_self_bite(self):
        head = self.snake.body[0]
        for module in self.snake.body[1:]:
            if module == head:
                return True
        return False

    def check_hit_border(self):
        head = self.snake.body[0]
        if (
            head[0] == 0 or
            head[0] == self.board.cols - 1 or
            head[1] == 0 or
            head[1] == self.board.rows - 1
        ):
            return True
        return False

    def check_apple(self):
        if (
            self.snake.body[0][0] == self.apple.y and
            self.snake.body[0][1] == self.apple.x
        ):
            return True
        return False

    def start(self):
        while True:
            global blocked_keyboard
            blocked_keyboard = False
            self.snake.set_dir(direction)
            self.snake.move()
            self.board.update(self.snake, self.apple)
            if self.check_self_bite():
                self.printer.clear_console()
                self.printer.print_bit()
                self.printer.print_score(self.points)
                break
            if self.check_hit_border():
                self.printer.clear_console()
                self.printer.print_crashed()
                self.printer.print_score(self.points)
                break
            if self.check_apple():
                self.printer.clear_console()
                self.points += self.apple_counter
                self.apple_counter += 1
                self.apple.create(self.board)
                self.snake.add_module()
                self.board.update(self.snake, self.apple)

            self.printer.clear_console()
            self.printer.print_score_tab(self.apple_counter - 1, self.points, len(self.snake.body))
            self.printer.print_board(self.board)
            print_colours_bar()
            sleep(self.delay)
