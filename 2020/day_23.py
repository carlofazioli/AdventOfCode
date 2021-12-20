class CupGame:
    def __init__(self, cups):
        self.cups = list(map(int, cups))

    def print(self):
        print('{} {} {} {} {} {} {} {} {}'.format(*self.cups))

    def output(self):
        idx = self.cups.index(1)
        a = self.cups[idx+1:] + self.cups[:idx]
        print(''.join(map(str, a)))

    def sim(self):
        c = self.cups[0]
        cut = self.cups[1:4]
        rem = self.cups[4:]
        d = c-1
        d %= 10
        while d not in rem:
            d -= 1
            d %= 10
        idx = rem.index(d)
        self.cups = rem[:idx+1] + cut + rem[idx+1:] + [c]


if __name__ == '__main__':
    cups = '398254716'
    g = CupGame(cups)
    g.print()
    for _ in range(10):
        g.sim()
    g.output()
    for _ in range(90):
        g.sim()
    g.output()