from game import Game, on_press
from pynput.keyboard import Listener
from printer import clear_console


def main():
    with Listener(on_press=on_press) as lis:
        clear_console()
        game = Game(8, 30, 30, 2, 5)
        game.menu()
        Listener.stop(lis)


if __name__ == '__main__':
    main()
