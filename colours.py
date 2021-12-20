colours = {
    'W': '\033[0m',  # white (normal)
    'R': '\033[31m',  # red
    'G': '\033[32m',  # green
    'Y': '\033[33m',  # yellow
    # 'B': '\033[34m',  # blue
    'M': '\033[35m',  # magenta
    # 'C': '\033[36m',  # cyan
}


def print_colours_bar():
    for key, colour in colours.items():
        print(f'{colour}██{colours["W"]}', end='')
    print()

