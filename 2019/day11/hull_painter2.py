import argparse
from intcode import IntCodeComputer


class Hull:
    def __init__(self):
        self.direction = 0
        self.loc = (0, 0)
        self.hull = {
            (0, 0): 0,
        }
        self.movements = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0),
        }
        self.has_painted = 0

    def update(self, painter_response):
        # Paint the current location:
        old_color = self.hull[self.loc]
        self.hull[self.loc] = painter_response[0]
        new_color = self.hull[self.loc]
        if new_color != old_color:
            self.has_painted += 1

        # Rotate:
        self.direction += (-1 + 2*painter_response[1])
        self.direction %= 4

        # Move forward 1:
        new_x = self.loc[0] + self.movements[self.direction][0]
        new_y = self.loc[1] + self.movements[self.direction][1]
        self.loc = (new_x, new_y)
        if self.loc not in self.hull:
            self.hull[self.loc] = 0

        return self.hull[self.loc]


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', dest='source', default='input')
    args = parser.parse_args()

    h = Hull()
    pc = IntCodeComputer(args.source, buffered=True)

    inp = 0
    response = pc.run(inp)

    while response:

        inp = h.update(response)
        pc.run(inp)

        print(len(h.hull))

    input()
