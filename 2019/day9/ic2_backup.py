def pad_modes(modes, n):
    return modes + [0] * (n - len(modes))


class IntCodeMem:
    def __init__(self,
                 source=None):
        self.mem = []
        if source:
            self.load(source)

    def load(self, source):
        with open(source) as f:
            mem_str = f.readline()
        mem_str.rstrip('\r\n')
        self.mem = list(map(int, mem_str.split(',')))

    def get(self, loc):
        assert loc >= 0, 'Attempting to access negative memory location!'
        if loc > len(self.mem):
            self.mem += [0] * (loc - len(self.mem) + 1)
        return self.mem[loc]

    def put(self, val, loc):
        assert loc >= 0, 'Attempting to access negative memory location!'
        if loc >= len(self.mem):
            self.mem += [0] * (loc - len(self.mem) + 1)
        self.mem[loc] = val


class IntCodeComp:
    def __init__(self,
                 source=None):
        self.mem = IntCodeMem(source)
        self.head = 0
        self.rel_base = 0
        self.codes = {
            1: self.add,
            2: self.mult,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adj_rel_base,
            99: self.exit,
        }

    # Operation:
    def run(self):
        while True:
            exit_code = self.execute_op()
            if exit_code < 0:
                break
        self.head = 0

    def execute_op(self):
        op_raw = self.read(mode=1)
        op_s = str(op_raw)
        code = int(op_s[-2:])
        modes_s = op_s[:-2][::-1]
        modes = list(map(int, list(modes_s)))
        return self.codes[code](modes)

    # Memory Interface:
    def read(self, mode=0):
        address = None
        if mode == 0:
            address = self.mem.get(self.head)
        if mode == 1:
            address = self.head
        if mode == 2:
            address = self.mem.get(self.head) + self.rel_base
        self.head += 1
        assert address is not None
        return self.mem.get(address)

    def write(self, val, mode=0):
        address = None
        if mode == 0:
            address = self.mem.get(self.head)
        if mode == 2:
            address = self.mem.get(self.head) + self.rel_base
        assert address is not None
        self.mem.put(val, address)
        self.head += 1

    # Instructions:
    def add(self, modes):
        n = 3
        modes = pad_modes(modes, n)
        op0 = self.read(mode=modes[0])
        op1 = self.read(mode=modes[1])
        self.write(op0 + op1, mode=modes[2])
        return 0

    def mult(self, modes):
        n = 3
        modes = pad_modes(modes, n)
        op0 = self.read(mode=modes[0])
        op1 = self.read(mode=modes[1])
        self.write(op0 * op1, mode=modes[2])
        return 0

    def input(self, modes):
        n = 1
        modes = pad_modes(modes, n)
        i = input()
        self.write(int(i), mode=modes[0])
        return 0

    def output(self, modes):
        n = 1
        modes = pad_modes(modes, n)
        print(self.read(mode=modes[0]))
        return 0

    def jump_if_true(self, modes):
        n = 2
        modes = pad_modes(modes, n)
        test = self.read(mode=modes[0])
        dest = self.read(mode=modes[1])
        if test:
            self.head = dest
        return 0

    def jump_if_false(self, modes):
        n = 2
        modes = pad_modes(modes, n)
        test = self.read(mode=modes[0])
        dest = self.read(mode=modes[1])
        if test == 0:
            self.head = dest
        return 0

    def less_than(self, modes):
        n = 3
        modes = pad_modes(modes, n)
        op0 = self.read(mode=modes[0])
        op1 = self.read(mode=modes[1])
        if op0 < op1:
            self.write(1, mode=modes[2])
        else:
            self.write(0, mode=modes[2])
        return 0

    def equals(self, modes):
        n = 3
        modes = pad_modes(modes, n)
        op0 = self.read(mode=modes[0])
        op1 = self.read(mode=modes[1])
        if op0 == op1:
            self.write(1, modes[2])
        else:
            self.write(0, modes[2])
        return 0

    def adj_rel_base(self, modes):
        n = 1
        modes = pad_modes(modes, n)
        op0 = self.read(mode=modes[0])
        self.rel_base += op0
        return 0

    @staticmethod
    def exit(exit_modes):
        if exit_modes is None:
            exit_modes = []
        return -1

