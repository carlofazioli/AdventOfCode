from collections import defaultdict


class BugMap:
    dirs = {
        0: (0, 1, 0),
        1: (0, -1, 0),
        2: (1, 0, 0),
        3: (-1, 0, 0),
    }

    def __init__(self,
                 source):
        with open(source) as f:
            lines = [line.strip('\r\n') for line in f]
        self.bugmap = dict()

        for y in range(5):
            for x in range(5):
                self.bugmap[(x, y, 0)] = lines[y][x]

        self.min_level = 0
        self.max_level = 0

    def init_level(self, level):
        for y in range(5):
            for x in range(5):
                self.bugmap[(x, y, level)] = '.'
        self.bugmap[(2, 2, level)] = '?'

    def neighbors(self, loc):
        x, y, z = loc

        n = []

        # Left neighbors:
        if x == 0:
            n += [(1, 2, z + 1)]
        elif x == 3:
            for j in range(5):
                n += [(4, j, z - 1)]
        else:
            n += x - 1, y, z

        # Right neighbors:
        if x == 4:
            n += [(3, 2, z + 1)]
        elif x == 1:
            for j in range(5):
                n += [(0, j, z - 1)]
        else:
            n += [(x + 1, y, z)]

        # Lower neighbors:
        if y == 0:
            n += [(2, 1, z + 1)]
        elif y == 3:
            for i in range(5):
                n += [(i, 4, z - 1)]
        else:
            n += [(x, y - 1, z)]

        # Upper neighbors:
        if y == 4:
            n += [(2, 3, z + 1)]
        elif y == 1:
            for i in range(5):
                n += [(i, 0, z - 1)]
        else:
            n += [(x, y + 1, z)]

        return n

    def __getitem__(self, item):
        return self.bugmap.get(item) == '#'

    def count_adj(self, loc):
        count = 0
        hood = self.neighbors(loc)
        for n in hood:
            count += self[n]
        return count

    def total_bugs(self):
        c = 0
        for loc in self.bugmap.keys():
            c += self[loc]
        return c

    def update(self):
        self.init_level(self.min_level - 1)
        self.min_level -= 1
        self.init_level(self.max_level + 1)
        self.max_level += 1

        newmap = dict()
        for loc in self.bugmap.keys():
            c = self.count_adj(loc)
            if self.bugmap[loc] == '.' and (c == 1 or c == 2):
                newmap[loc] = '#'
            elif self[loc] and (c != 1):
                newmap[loc] = '.'
            else:
                newmap[loc] = self.bugmap[loc]
        self.bugmap = newmap

    def display(self):
        for level in range(self.min_level, self.max_level + 1):
            print('Level: ', level)
            for y in range(5):
                row = []
                for x in range(5):
                    row.append(self.bugmap.get((x, y, level), '?'))
                print(''.join(row))
            print()


if __name__ == '__main__':

    m = BugMap('test2')

    for t in range(10):
        m.update()
        m.display()

    # done = None
    # while not done:
    #     done = m.update()
    #
    # print(done)
    input()


