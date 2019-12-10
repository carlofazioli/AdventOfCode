class TuringTape:
    def __init__(self):
        self.mem = []

    def __getitem__(self, item):
        if item >= len(self.mem):
            self.mem += [0] * (item - len(self.mem) + 1)
        return self.mem[item]
