import os
from time import sleep

from pynput.keyboard import Key

from board import Board, print_colours_bar
from snake import Snake
from apple import Apple


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


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


class Game:

    def __init__(self, fps, x, y, snake_speed, snake_length):
        clear_console()
        self.logo = ''
        with open('assets/logo.txt', 'r') as logo:
            for line in logo.readlines():
                self.logo += line
        print('\n\n\n\n\n', self.logo)
        self.delay = 1/fps
        self.board = Board(x, y)
        self.snake = Snake(snake_length, int(x/2), int(y/2))
        self.timer = 0
        self.apples = 1
        self.points = 0
        self.snake_speed = snake_speed
        self.apple = Apple(self.board)
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
                print('you bit yourself')
                break
            if self.check_hit_border():
                print('you hit the border')
                break
            if self.check_apple():
                self.points += self.apples
                self.apples += 1
                self.apple.create(self.board)
                self.snake.add_module()
                self.board.update(self.snake, self.apple)

            clear_console()
            print(
                f'jabłko: {self.apples} \tpunkty: {self.points}\trozmiar: {len(self.snake.body)}'
            )
            print(self.board.render())
            print_colours_bar()
            sleep(self.delay)
