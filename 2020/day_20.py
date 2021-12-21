class Tile:
    flip_lookup = dict()

    def __init__(self, raw_tile):
        tile = raw_tile.split('\n')
        title = tile.pop(0)
        self.id = int(title[5:9])
        self.tile = [list(row) for row in tile]
        assert len(tile) == 10
        assert len(tile[0]) == 10
        self.neighbors = dict()
        self.signature = list()
        self.t = None
        self.b = None
        self.r = None
        self.l = None
        self.setup()

    def setup(self):
        t = ''.join(self.tile[0])
        b = ''.join(self.tile[-1])
        r = ''.join([row[-1] for row in self.tile])
        l = ''.join([row[0] for row in self.tile])
        t = self.convert(t)
        b = self.convert(b)
        r = self.convert(r)
        l = self.convert(l)
        self.t = t
        self.b = b
        self.r = r
        self.l = l
        for val in [t, b, r, l]:
            self.signature.append(val)
            self.signature.append(self.flip_val(val))

    def flip(self):
        self.tile = [row[::-1] for row in self.tile]
        self.t = self.flip_val(self.t)
        self.b = self.flip_val(self.b)
        self.l, self.r = self.r, self.l

    def rotate(self):
        self.tile = [[self.tile[j][9-i] for j in range(10)] for i in range(10)]
        t, r, b, l = self.t, self.r, self.b, self.l
        self.t, self.r, self.b, self.l = r, b, l, t

    @staticmethod
    def convert(s):
        s = s.replace('.', '0').replace('#', '1')
        return int(s, 2)

    def flip_val(self, i):
        if i in self.flip_lookup:
            return self.flip_lookup[i]
        else:
            b = int(bin(i)[2:].zfill(10)[::-1], 2)
            self.flip_lookup[i] = b
            self.flip_lookup[b] = i
            return b

    def print(self):
        for row in self.tile:
            print(''.join(row))


class Image:
    def __init__(self, raw_tiles_list):
        self.tiles = dict()
        self.interior = dict()
        self.boundary = dict()
        self.corner = dict()
        self.sigs = []
        for raw_tile in raw_tiles_list:
            t = Tile(raw_tile)
            self.tiles[t.id] = t
            self.sigs += t.signature
        self.grid = [[None]*12 for _ in range(12)]
        self.candidates = []

    def check_matches(self, t):
        hits = 0
        for v in t.signature:
            idx = self.sigs.index(v)
            hits += v in self.sigs[idx+1:]
        return hits

    def find_corners(self):
        prod = 1
        for id, tile in self.tiles.items():
            hits = self.check_matches(tile)
            if hits == 4:
                self.corner[id] = tile
                prod *= id
            if hits == 6:
                self.boundary[id] = tile
            if hits == 8:
                self.interior[id] = tile
        return prod

    @staticmethod
    def are_adj(t0, t1):
        s0 = set(t0.signature)
        s1 = set(t1.signature)
        return s0.intersection(s1)

    def populate_grid(self):
        print('(0, 0) ', end='')
        self.grid[0][0] = self.corner.popitem()[1]
        # Hardcoded, determined by hand:
        self.grid[0][0].rotate()
        self.grid[0][0].rotate()
        self.grid[0][0].flip()
        # Match top row:
        for col in range(1, 11):
            # Top row is in the boundary set:
            for i, c in self.boundary.items():
                if self.are_adj(self.grid[0][col-1], c):
                    if self.match_right(self.grid[0][col-1], c):
                        self.grid[0][col] = c
                        print(f'(0, {col}) ', end='')
                        break
            self.boundary.pop(i)
        # End of top row is in the corner set:
        for i, c in self.corner.items():
            if self.are_adj(self.grid[0][10], c):
                if self.match_right(self.grid[0][10], c):
                    self.grid[0][11] = c
                    print('(1, 11)')
                    break
        self.corner.pop(i)
        # Match middle rows:
        for row in range(1, 11):
            # Find leftmost in row from boundary tiles:
            for i, c in self.boundary.items():
                if self.are_adj(self.grid[row-1][0], c):
                    if self.match_bottom(self.grid[row-1][0], c):
                        self.grid[row][0] = c
                        print(f'({row}, 0) ', end='')
                        break
            self.boundary.pop(i)
            # Fill in row from interior tiles:
            for col in range(1, 11):
                found = False
                for i, c in self.interior.items():
                    if self.are_adj(self.grid[row][col-1], c):
                        if self.match_right(self.grid[row][col-1], c):
                            self.grid[row][col] = c
                            print(f'({row}, {col}) ', end='')
                            found = True
                            break
                assert found
                self.interior.pop(i)
            # End the row with a boundary tile:
            for i, c in self.boundary.items():
                if self.are_adj(self.grid[row][10], c):
                    if self.match_right(self.grid[row][10], c):
                        self.grid[row][11] = c
                        print(f'({row}, 11)')
                        break
            self.boundary.pop(i)
        # Bottom left:
        for i, c in self.corner.items():
            if self.are_adj(self.grid[10][0], c):
                if self.match_bottom(self.grid[10][0], c):
                    self.grid[11][0] = c
                    print('(11, 0) ', end='')
                    break
        self.corner.pop(i)
        for col in range(1, 11):
            for i, c in self.boundary.items():
                if self.are_adj(self.grid[11][col - 1], c):
                    if self.match_right(self.grid[11][col - 1], c):
                        self.grid[11][col] = c
                        print(f'(11, {col}) ', end='')
                        break
            self.boundary.pop(i)
        i, c = self.corner.popitem()
        self.match_right(self.grid[11][10], c)
        self.grid[11][11] = c
        print('(11, 11)')

    @staticmethod
    def match_right(t, c):
        comps = 0
        while t.r != c.l:
            comps += 1
            c.rotate()
            if comps == 4:
                c.flip()
                c.rotate()
                c.flip()
            if comps == 9:
                return False
        return True

    @staticmethod
    def match_bottom(t, c):
        comps = 0
        while t.b != c.t:
            comps += 1
            c.rotate()
            if comps == 4:
                c.flip()
                c.rotate()
                c.flip()
            if comps == 9:
                return False
        return True






if __name__ == '__main__':
    with open('input_data/day_20.txt') as f:
        raw = f.read()
    raw_tiles_list = raw.split('\n\n')
    img = Image(raw_tiles_list)
    p = img.find_corners()
    img.populate_grid()