from game import Game, on_press
from pynput.keyboard import Listener
import threading
import sys

from printer import clear_console

def game_t():
    clear_console()
    game = Game(8, 30, 30, 2, 5)
    game.menu()


def listener():
    with Listener(on_press=on_press) as lis:
        lis.join()


def main():
    workers = [
        threading.Thread(target=listener, args=()).start(),
        threading.Thread(target=game_t, args=()).start(),
    ]


if __name__ == '__main__':
    main()
