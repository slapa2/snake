import os
import time

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
            f'apple: {apples} \tpoints: {points}\tsnake length: {snake_len}'
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
    def clear_console():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def print_logo(self):
        print(self.logo_str)

    def print_score(self, score):
        print(self._concatenate_chars([
            self.score_str, self.space_str, self.get_number_str(score)
        ]))

    def get_number_str(self, number):
        score_arr = [x for x in str(number)]
        score_str_arr = [self.numbers[x] for x in score_arr]
        return self._concatenate_chars(score_str_arr)

    @staticmethod
    def _split_str(string):
        return string.split('\n')

    def _concatenate_chars(self, array):
        str_split_arr = [self._split_str(x) for x in array]
        zip_arr = zip(*str_split_arr)
        joined_lines = [''.join(x) for x in zip_arr]
        return '\n'.join(joined_lines)

    def print_crashed(self):
        print(self.game_over_str)
        print(self.crashed_str)

    def print_bit(self):
        print(self.game_over_str)
        print(self.bit_str)

    def print_all_numbers(self):
        for number in self.numbers.values():
            self.clear_console()
            print(number)
            time.sleep(1)
