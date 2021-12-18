from game import Game, on_press
from pynput.keyboard import Listener
import threading


def game_t():
    game = Game(24, 50, 50, 2, 5)
    game.start()


def listener():
    with Listener(on_press=on_press) as l:
        l.join()


def main():

    t1 = threading.Thread(target=listener, args=()).start()
    t2 = threading.Thread(target=game_t, args=()).start()


if __name__ == '__main__':
    main()
