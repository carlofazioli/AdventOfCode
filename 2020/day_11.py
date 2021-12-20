import pkg_resources

import utilities


seating = utilities.input_to_list('day_11.txt')


class SeatingMap:
    def __init__(self, m):
        self.m = [list(row) for row in m]
        self.w = len(m[0])
        self.h = len(m)
        self.new_m = None

    def __getitem__(self, item):
        i = item[0]
        j = item[1]
        if 0 <= i < self.w and 0 <= j < self.h:
            return self.m[j][i]
        return None

    def __setitem__(self, key, value):
        i = key[0]
        j = key[1]
        if 0 <= i < self.w and 0 <= j < self.h:
            self.m[j][i] = value

    def count_seats(self):
        count = 0
        for i in range(self.w):
            for j in range(self.h):
                count += self[i, j] == '#'
        return count

    def count_adj_occupied(self, i, j):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                count += self[i+dx, j+dy] == '#'
        return count

    def update_map(self):
        changed = False
        self.new_m = [['.']*self.w for _ in range(self.h)]
        for i in range(self.w):
            for j in range(self.h):
                if self[i, j] == '.':
                    continue
                k = self.count_adj_occupied(i, j)
                if self[i, j] == 'L':
                    if k == 0:
                        self.new_m[j][i] = '#'
                        changed = True
                    else:
                        self.new_m[j][i] = 'L'
                if self[i, j] == '#':
                    if k >= 4:
                        self.new_m[j][i] = 'L'
                        changed = True
                    else:
                        self.new_m[j][i] = '#'
        self.m = self.new_m
        self.new_m = None
        return changed

    def print(self):
        s = ''
        for row in self.m:
            s += ''.join(row) + '\n'
        print(s)


# s = SeatingMap(seating)
# changed = True
# while changed:
#     print(s.count_seats())
#     changed = s.update_map()
#
# print(s.count_seats())


class SeatingMap2:
    def __init__(self, m):
        self.m = [list(row) for row in m]
        self.w = len(m[0])
        self.h = len(m)
        self.new_m = None

    def __getitem__(self, item):
        i = item[0]
        j = item[1]
        if 0 <= i < self.w and 0 <= j < self.h:
            return self.m[j][i]
        return None

    def __setitem__(self, key, value):
        i = key[0]
        j = key[1]
        if 0 <= i < self.w and 0 <= j < self.h:
            self.m[j][i] = value

    def count_seats(self):
        count = 0
        for i in range(self.w):
            for j in range(self.h):
                count += self[i, j] == '#'
        return count

    def count_adj_occupied(self, i, j):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                d = 1
                while True:
                    next_spot = self[i+d*dx, j+d*dy]
                    if next_spot is None or next_spot == 'L':
                        break
                    if next_spot == '.':
                        d += 1
                    if next_spot == '#':
                        count += 1
                        break
        return count

    def update_map(self):
        changed = False
        self.new_m = [['.']*self.w for _ in range(self.h)]
        for i in range(self.w):
            for j in range(self.h):
                if self[i, j] == '.':
                    continue
                k = self.count_adj_occupied(i, j)
                if self[i, j] == 'L':
                    if k == 0:
                        self.new_m[j][i] = '#'
                        changed = True
                    else:
                        self.new_m[j][i] = 'L'
                if self[i, j] == '#':
                    if k >= 5:
                        self.new_m[j][i] = 'L'
                        changed = True
                    else:
                        self.new_m[j][i] = '#'
        self.m = self.new_m
        self.new_m = None
        return changed

    def print(self):
        s = ''
        for row in self.m:
            s += ''.join(row) + '\n'
        print(s)


example_seating = [
'L.LL.LL.LL',
'LLLLLLL.LL',
'L.L.L..L..',
'LLLL.LL.LL',
'L.LL.LL.LL',
'L.LLLLL.LL',
'..L.L.....',
'LLLLLLLLLL',
'L.LLLLLL.L',
'L.LLLLL.LL',
]
s2 = SeatingMap2(seating)
changed = True
while changed:
    print(s2.count_seats())
    # s2.print()
    changed = s2.update_map()
