from time import sleep
from pynput.keyboard import Key, Listener

from board import Board
from snake import Snake
from apple import Apple
from colours import print_colours_bar
from printer import Printer, clear_console

direction = "UP"
blocked_keyboard = False


def on_press(key=None):

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
        self.printer = Printer()
        self.delay = 1 / fps
        self.snake_speed = snake_speed
        self.board_size = (x, y)
        self.snake_length = snake_length
        self.board = None
        self.snake = None
        self.apple_counter = None
        self.points = None
        self.apple = None

    def new_game(self):
        self.board = None
        self.snake = None
        self.apple_counter = None
        self.points = None
        self.apple = None
        self.apple_counter = 1
        self.points = 0

        self.board = Board(*self.board_size)
        self.snake = Snake(
            self.snake_length,
            int(self.board_size[0] / 2), int(self.board_size[1] / 2))
        self.apple = Apple(self.board)

        for i in reversed(range(1, 3)):
            clear_console()
            print(self.printer.logo_str)
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
            clear_console()
            self.points += self.apple_counter
            self.apple_counter += 1
            self.apple.create(self.board)
            self.snake.add_module()
            self.board.update(self.snake, self.apple)
            return True
        return False

    def refresh_board(self):
        clear_console()
        self.printer.print_score_tab(self.apple_counter - 1, self.points, len(self.snake.body))
        self.printer.print_board(self.board)
        print_colours_bar()

    def end_game(self, reason):
        sleep(1)
        clear_console()
        print(self.printer.game_over_str)
        if reason == 'crashed':
            print(self.printer.crashed_str)
            self.printer.print_score(self.points)
        elif reason == 'bit':
            print(self.printer.bit_str)
            self.printer.print_score(self.points)

    def start(self):
        global blocked_keyboard
        self.new_game()
        while True:
            blocked_keyboard = False
            self.snake.set_dir(direction)
            self.snake.move()
            self.board.update(self.snake, self.apple)
            if self.check_self_bite():
                self.end_game('bit')
                return
            if self.check_hit_border():
                self.end_game('crashed')
                return
            self.check_apple()
            self.refresh_board()
            sleep(self.delay)

    def menu(self):
        with Listener(on_press=on_press) as listener:
            while True:
                print(self.printer.menu_str)
                selected = input('Select option and pres Enter: ')[-1]
                if selected == '1':
                    self.start()
                    continue
                elif selected == '2':
                    return
                elif selected == '0':
                    return
                else:
                    print('Wrong option try again!')


def main():
    game = Game(8, 30, 30, 2, 5)
    game.menu()


if __name__ == '__main__':
    main()

