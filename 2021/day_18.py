import itertools

from utilities import load_data


YEAR = 2021
DAY = 18
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


class SnailFishNumber:
    def __init__(self, s, parent=None):
        self.parent = parent
        if isinstance(s, str):
            s = eval(s)
        if isinstance(s, list):
            assert len(s) == 2
            self.L = SnailFishNumber(s[0], self)
            self.R = SnailFishNumber(s[1], self)
            self.pair = True
        elif isinstance(s, int):
            self.pair = False
            self.val = s
        else:
            raise RuntimeError

    def re_init(self, s):
        self.__init__(s, parent=self.parent)

    def depth(self):
        if not self.pair:
            return 0
        if self.parent is not None:
            return self.parent.depth() + 1
        else:
            return 0

    def print(self):
        if self.pair:
            return f'[{self.L.print()},{self.R.print()}]'
        else:
            return str(self.val)

    def walk(self):
        queue = []
        if self.L.pair:
            queue = self.L.walk() + queue
        queue += [self]
        if self.R.pair:
            queue += self.R.walk()
        return queue

    def update_left(self, sfn):
        current = self
        parent = self.parent
        if parent is None:
            return None
        while current == parent.L:
            current = parent
            parent = parent.parent
            if parent is None:
                return None
        current = parent.L
        while current.pair:
            current = current.R
        current.val += sfn.val

    def update_right(self, sfn):
        current = self
        parent = self.parent
        if parent is None:
            return None
        while current == parent.R:
            current = parent
            parent = parent.parent
            if parent is None:
                return None
        current = parent.R
        while current.pair:
            current = current.L
        current.val += sfn.val

    def reduce(self):
        reduced = False
        while not reduced:
            exploded = False
            split = False
            queue = self.walk()
            for sfn in queue:
                if sfn.depth() == 4:
                    a, b = sfn.L, sfn.R
                    sfn.re_init(0)
                    sfn.update_left(a)
                    sfn.update_right(b)
                    exploded = True
                    break
            if exploded:
                reduced = False
                continue
            for sfn in queue:
                if not sfn.L.pair and sfn.L.val >= 10:
                    sfn.L.re_init([sfn.L.val//2, (sfn.L.val+1)//2])
                    split = True
                    break
                if not sfn.R.pair and sfn.R.val >= 10:
                    sfn.R.re_init([sfn.R.val//2, (sfn.R.val+1)//2])
                    split = True
                    break
            if not exploded and not split:
                reduced = True

    def __add__(self, other):
        s = f'[{self.print()},{other.print()}]'
        s = SnailFishNumber(eval(s))
        s.reduce()
        return s

    def magnitude(self):
        if self.pair:
            return 3*self.L.magnitude() + 2*self.R.magnitude()
        else:
            return self.val


s = SnailFishNumber(input_data[0])
for t in input_data[1:]:
    s += SnailFishNumber(t)
print(s.magnitude())

m = 0
sfns = [SnailFishNumber(s) for s in input_data]
for x, y in itertools.combinations(sfns, 2):
    m = max((x+y).magnitude(), m)
    m = max((y+x).magnitude(), m)
print(m)