from math import gcd, atan


class AsteroidField:
    def __init__(self,
                 source,
                 lazer=None):
        self.field = list()
        if isinstance(source, str):
            with open(source) as f:
                for line in f:
                    self.field.append(line.rstrip('\r\n'))
        self.width = len(self.field[0])
        self.height = len(self.field)
        self.dirs = self.build_dirs()
        self.lazer = lazer

    def build_dirs(self):
        dirs = set()
        for x in range(self.width):
            for y in range(self.height):
                if x == y == 0:
                    continue
                m = gcd(x, y)
                nx = x // m
                ny = y // m
                dirs |= {(nx, ny)}
        dirs = list(dirs)
        dirs = sorted(dirs, key=lambda v: atan(v[1]/(v[0]+0.00000001)), reverse=True)
        # dirs[0], dirs[-1] = dirs[-1], dirs[0]
        return dirs

    def parse_roids(self):
        max_sight = 0
        max_x = None
        max_y = None
        for ass_x in range(self.width):
            for ass_y in range(self.height):
                if self.field[ass_y][ass_x] == '.':
                    continue
                count = 0
                for v in self.dirs:
                    count += self.line_of_sight(ass_x, ass_y,  v[0],  v[1])
                    count += self.line_of_sight(ass_x, ass_y, -v[0], -v[1])
                    if v[0] != 0 and v[1] != 0:
                        count += self.line_of_sight(ass_x, ass_y, -v[0],  v[1])
                        count += self.line_of_sight(ass_x, ass_y,  v[0], -v[1])
                if count > max_sight:
                    max_sight = count
                    max_x = ass_x
                    max_y = ass_y
        return max_x, max_y, max_sight

    def do_the_lazer(self):
        shot = 0
        while True:
            for v in self.dirs:
                hit, x, y = self.lazer_shot(v[0], -v[1])
                shot += hit
                if shot == 200:
                    return x, y
            for v in reversed(self.dirs[:-1]):
                hit, x, y, = self.lazer_shot(v[0], v[1])
                shot += hit
                if shot == 200:
                    return x, y
            for v in self.dirs[1:]:
                hit, x, y = self.lazer_shot(-v[0], v[1])
                shot += hit
                if shot == 200:
                    return x, y
            for v in reversed(self.dirs[1:-1]):
                hit, x, y = self.lazer_shot(-v[0], -v[1])
                shot += hit
                if shot == 200:
                    return x, y

    def lazer_shot(self, dx, dy):
        for k in range(1, max(self.height, self.width)):
            tx = self.lazer[0] + k*dx
            ty = self.lazer[1] + k*dy
            if self.in_bounds(tx, ty) and self.field[ty][tx] == '#':
                tmp = self.field[ty]  # This is the row
                tmp = list(tmp)
                tmp[tx] = '.'
                self.field[ty] = ''.join(tmp)
                print(tx, ty)
                return 1, tx, ty
        return 0, None, None

    def line_of_sight(self, x, y, dx, dy):
        for k in range(1, max(self.height, self.width)):
            tx = x + k*dx
            ty = y + k*dy
            if self.in_bounds(tx, ty) and self.field[ty][tx] == '#':
                return 1
        return 0

    def in_bounds(self, a, b):
        return a in range(self.width) and b in range(self.height)


if __name__ == '__main__':

    ass = AsteroidField('input', [20, 19])
    # X, Y, Z = ass.parse_roids()

    # print(X, Y, Z)

    print(ass.do_the_lazer())
    input()