class Snake:

    def __init__(self, length, x, y):
        self.body = [(x, y + i) for i in range(length)]
        self.dir = (0, -1)

    def set_dir(self, direction):
        if direction == 'up':
            self.dir = (0, -1)
        elif direction == 'down':
            self.dir = (0, 1)
        elif direction == 'right':
            self.dir = (1, 0)
        elif direction == 'left':
            self.dir = (-1, 0)
        else:
            raise Exception

    def move(self):

        for i in reversed(range(len(self.body))):
            if i != 0:
                self.body[i] = self.body[i - 1]
            else:
                self.body[i] = tuple(map(lambda a, b: a + b, self.body[i], self.dir))

