import os
import time


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


class Printer:

    def __init__(self):

        self.logo_str = '\n\n\n\n\n'
        with open('assets/logo.txt', 'r') as logo:
            for line in logo.readlines():
                self.logo_str += line

        self.bit_str = ''
        with open('assets/bit.txt', 'r') as bit:
            for line in bit.readlines():
                self.bit_str += line

        self.bit_str = ''
        with open('assets/bit.txt', 'r') as bit:
            for line in bit.readlines():
                self.bit_str += line

        self.crashed_str = ''
        with open('assets/crashed.txt', 'r') as crashed:
            for line in crashed.readlines():
                self.crashed_str += line

        self.game_over_str = '\n\n'
        with open('assets/game_over.txt', 'r') as game_over:
            for line in game_over.readlines():
                self.game_over_str += line

        self.score_str = ''
        with open('assets/score.txt', 'r') as score:
            for line in score.readlines():
                self.score_str += line

        self.space_str = ''
        with open('assets/space.txt', 'r') as space:
            for line in space.readlines():
                self.space_str += line

        self.menu_str = ''
        with open('assets/menu.txt', 'r') as menu:
            for line in menu.readlines():
                self.menu_str += line

        self.numbers = {
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '0': '',
        }

        for number in self.numbers:
            with open(f'assets/{number}.txt', 'r') as f:
                for line in f.readlines():
                    self.numbers[number] += line

    @staticmethod
    def print_score_tab(apples, points, snake_len):
        print(
            f'apples: {apples} \tpoints: {points}\tsnake length: {snake_len}'
        )

    @staticmethod
    def print_board(board):
        render = ''
        for row in board.board:
            for i, col in enumerate(row):
                render += col
            render += '\n'
        print(render)

    @staticmethod
    def _concatenate_chars(array):
        str_split_arr = [x.split('\n') for x in array]
        zip_arr = zip(*str_split_arr)
        joined_lines = [''.join(x) for x in zip_arr]
        return '\n'.join(joined_lines)

    def print_logo(self):
        print(self.logo_str)

    def print_score(self, score):
        print(self._concatenate_chars([
            self.score_str, self.space_str, self._get_number_str(score)
        ]))

    def print_number(self, number):
        print(self._concatenate_chars(
            [self.space_str for _ in range(26)] + [self._get_number_str(number)]))

    def _get_number_str(self, number):
        score_arr = [x for x in str(number)]
        score_str_arr = [self.numbers[x] for x in score_arr]
        return self._concatenate_chars(score_str_arr)

    def print_crashed(self):
        print(self.crashed_str)

    def print_game_over(self):
        print(self.game_over_str)

    def print_bit(self):
        print(self.bit_str)

    def print_all_numbers(self):
        for number in self.numbers.values():
            clear_console()
            print(number)
            time.sleep(1)

    def print_menu(self):
        print(self.menu_str)


