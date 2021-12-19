import os
import time


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def get_str_form_file(file):
    string = ''
    with open(f'{file}', 'r') as f:
        for line in f.readlines():
            string += line
    return string


class Printer:

    def __init__(self):

        self.logo_str = '\n\n\n\n\n' + get_str_form_file('assets/logo.txt')
        self.bit_str = get_str_form_file('assets/bit.txt')
        self.crashed_str = get_str_form_file('assets/crashed.txt')
        self.game_over_str = '\n\n' + get_str_form_file('assets/game_over.txt')
        self.score_str = get_str_form_file('assets/score.txt')
        self.space_str = get_str_form_file('assets/space.txt')
        self.menu_str = get_str_form_file('assets/menu.txt')

        self.numbers = {x: '' for x in range(10)}
        for number in self.numbers:
            self.numbers[number] = get_str_form_file(f'assets/{number}.txt')

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




