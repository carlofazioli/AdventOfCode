import utilities


init_map = utilities.input_to_list('day_17.txt')


class Cube:
    def __init__(self, map):
        self.map = map
        self.m = dict()
        self.x_bounds = list()
        self.y_bounds = list()
        self.z_bounds = list()
        self.setup()

    def __getitem__(self, loc):
        return self.m.get(loc, '.')

    def __setitem__(self, loc, value):
        self.m[loc] = value

    def setup(self):
        w = len(self.map[0])
        h = len(self.map)
        self.x_bounds = [0, w]
        self.y_bounds = [0, h]
        self.z_bounds = [0, 1]
        for x in range(w):
            for y in range(h):
                loc = (x, y, 0)
                self[loc] = self.map[y][x]

    def count_adj_occupied(self, i, j, k):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    loc = (i + dx, j + dy, k + dz)
                    count += self[loc] == '#'
        return count

    def expand_bounds(self):
        self.x_bounds[0] -= 1
        self.x_bounds[1] += 1
        self.y_bounds[0] -= 1
        self.y_bounds[1] += 1
        self.z_bounds[0] -= 1
        self.z_bounds[1] += 1

    def update(self):
        changes = dict()
        self.expand_bounds()
        for x in range(*self.x_bounds):
            for y in range(*self.y_bounds):
                for z in range(*self.z_bounds):
                    loc = (x, y, z)
                    k = self.count_adj_occupied(*loc)
                    if self[loc] == '#':
                        if k < 2 or k > 3:
                            changes[loc] = '.'
                    if self[loc] == '.':
                        if k == 3:
                            changes[loc] = '#'
        for loc, val in changes.items():
            self[loc] = val

    def count(self):
        count = 0
        for val in self.m.values():
            count += val == '#'
        return count


c = Cube(init_map)
for _ in range(6):
    c.update()
print(c.count())


class HyperCube:
    def __init__(self, map):
        self.map = map
        self.m = dict()
        self.x_bounds = list()
        self.y_bounds = list()
        self.z_bounds = list()
        self.w_bounds = list()
        self.setup()

    def __getitem__(self, loc):
        return self.m.get(loc, '.')

    def __setitem__(self, loc, value):
        self.m[loc] = value

    def setup(self):
        w = len(self.map[0])
        h = len(self.map)
        self.x_bounds = [0, w]
        self.y_bounds = [0, h]
        self.z_bounds = [0, 1]
        self.w_bounds = [0, 1]
        for x in range(w):
            for y in range(h):
                loc = (x, y, 0, 0)
                self[loc] = self.map[y][x]

    def count_adj_occupied(self, i, j, k, m):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        loc = (i + dx, j + dy, k + dz, m + dw)
                        count += self[loc] == '#'
        return count

    def expand_bounds(self):
        self.x_bounds[0] -= 1
        self.x_bounds[1] += 1
        self.y_bounds[0] -= 1
        self.y_bounds[1] += 1
        self.z_bounds[0] -= 1
        self.z_bounds[1] += 1
        self.w_bounds[0] -= 1
        self.w_bounds[1] += 1

    def update(self):
        changes = dict()
        self.expand_bounds()
        for x in range(*self.x_bounds):
            for y in range(*self.y_bounds):
                for z in range(*self.z_bounds):
                    for w in range(*self.w_bounds):
                        loc = (x, y, z, w)
                        k = self.count_adj_occupied(*loc)
                        if self[loc] == '#':
                            if k < 2 or k > 3:
                                changes[loc] = '.'
                        if self[loc] == '.':
                            if k == 3:
                                changes[loc] = '#'
        for loc, val in changes.items():
            self[loc] = val

    def count(self):
        count = 0
        for val in self.m.values():
            count += val == '#'
        return count


h = HyperCube(init_map)
for _ in range(6):
    h.update()
print(h.count())
