import utilities


paths = utilities.input_to_list('day_24.txt')
# paths = utilities.input_to_list('day_24_example.txt')

directions = {
    'e': [1, 0],
    'ne': [0, 1],
    'se': [1, -1],
    'w': [-1, 0],
    'sw': [0, -1],
    'nw': [-1, 1]
}

tiles = dict()


def parse_path(p):
    x, y = 0, 0
    while p:
        d = p[0]
        p = p[1:]
        if d not in 'ew':
            d += p[0]
            p = p[1:]
        if d == 'e':
            x += 1
        if d == 'w':
            x -= 1
        if d == 'ne':
            y += 1
        if d == 'sw':
            y -= 1
        if d == 'se':
            x += 1
            y -= 1
        if d == 'nw':
            x -= 1
            y += 1
    if (x, y) not in tiles:
        tiles[(x, y)] = 'B'
    else:
        s = tiles[(x, y)]
        if s == 'B':
            tiles[(x, y)] = 'W'
        if s == 'W':
            tiles[(x, y)] = 'B'


for path in paths:
    parse_path(path)

count = 0
for val in tiles.values():
    count += val == 'B'
print(count)


class Hex:
    def __init__(self, tiles):
        self.m = dict(tiles)
        self.old_m = dict()

    def __getitem__(self, loc):
        return self.m.get(loc, 'W')

    def __setitem__(self, loc, value):
        self.m[loc] = value

    def count_adj_occupied(self, i, j):
        count = 0
        # count += self[(i+1, j)] == 'B'  # east
        # count += self[(i-1, j)] == 'B'  # west
        # count += self[(i+1, j-1)] == 'B'  # southeast
        # count += self[(i-1, j+1)] == 'B'  # northwest
        # count += self[(i, j+1)] == 'B'  # northeast
        # count += self[(i, j-1)] == 'B'  # southwest
        e = self[(i+1, j)]  # east
        ne = self[(i, j+1)]  # northeast
        nw = self[(i-1, j+1)]  # northwest
        w = self[(i-1, j)]  # west
        sw = self[(i, j-1)]  # southwest
        se = self[(i+1, j-1)]  # southeast
        for ch in [e, ne, nw, w, sw, se]:
            count += ch == 'B'
        return count

    def expand_bounds(self):
        for loc in list(self.m.keys()):
            x, y = loc
            self.add((x+1, y))
            self.add((x-1, y))
            self.add((x+1, y-1))
            self.add((x-1, y+1))
            self.add((x, y+1))
            self.add((x, y-1))

    def add(self, loc):
        if loc not in self.m:
            self[loc] = 'W'

    def update(self):
        self.expand_bounds()
        self.old_m = dict(self.m)
        changes = dict()
        for loc in list(self.m.keys()):
            k = self.count_adj_occupied(*loc)
            if self[loc] == 'B':
                if k == 0 or k > 2:
                    changes[loc] = 'W'
            if self[loc] == 'W':
                if k == 2:
                    changes[loc] = 'B'
        for loc, val in changes.items():
            self[loc] = val

    def count(self):
        count = 0
        for val in self.m.values():
            count += val == 'B'
        return count


h = Hex(tiles)

for i in range(100):

    h.update()
    if i+1 < 10 or (i+1) % 10 == 0:
        print(i+1, ':', h.count())


print(h.count())