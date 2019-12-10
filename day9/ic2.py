import argparse


class TuringTape:
    def __init__(self,
                 source=None):
        if isinstance(source, str):
            with open(source) as f:
                mem_str = f.readline()
            mem_str.rstrip('\r\n')
            self.mem = list(map(int, mem_str.split(',')))
        if isinstance(source, list):
            self.mem = source
        if source is None:
            self.mem = list()

    # If a TuringTape's memory is accessed out of bounds, grow it:
    def buffer_check(self, loc):
        assert loc >= 0, 'Attempting to access a negative memory location.'
        if loc >= len(self.mem):
            self.mem += [0] * (loc - len(self.mem) + 1)

    # Override the [] operators for get and set, so the tape acts like a list:
    def __getitem__(self, loc):
        self.buffer_check(loc)
        return self.mem[loc]

    def __setitem__(self, loc, val):
        self.buffer_check(loc)
        self.mem[loc] = val


class IntCodeComp:
    def __init__(self,
                 source=None):

        # Initialize the TuringTape
        self.tape = TuringTape(source)

        # Initialize the tape head and relative base:
        self.head = 0
        self.rel_base = 0

        # IntCode dictionary:
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

    # Main operation:
    def run(self):
        while True:
            # Fetch the current operation and its modes.
            # If its exit code is negative, break.
            exe, modes = self.parse_op()
            if exe(modes) < 0:
                break
        self.head = 0

    def parse_op(self):
        # Parse the tape head for the operation and its modes.
        # Lookup and return the executable, and the modes.
        op_raw = self.mem(mode=1)
        op_s = str(op_raw)
        op = int(op_s[-2:])
        modes_s = op_s[:-2][::-1]
        modes = list(map(int, list(modes_s)))
        return self.codes[op], modes

    # Memory Interface:
    # Obtain the appropriate address for the mode.
    # Read/write as indicated by a write_val.
    # Advance the tape head.
    def mem(self, write_val=None, mode=0):
        address = None
        if mode == 0:
            address = self.tape[self.head]
        if mode == 1:
            address = self.head
        if mode == 2:
            address = self.tape[self.head] + self.rel_base
        self.head += 1
        assert address is not None
        if write_val is not None:
            self.tape[address] = write_val
        else:
            return self.tape[address]

    # Instructions:
    def add(self, modes):
        n = 3
        modes = self.pad_modes(modes, n)
        op0 = self.mem(mode=modes[0])
        op1 = self.mem(mode=modes[1])
        self.mem(write_val=op0 + op1, mode=modes[2])
        return 0

    def mult(self, modes):
        n = 3
        modes = self.pad_modes(modes, n)
        op0 = self.mem(mode=modes[0])
        op1 = self.mem(mode=modes[1])
        self.mem(write_val=op0 * op1, mode=modes[2])
        return 0

    def input(self, modes):
        n = 1
        modes = self.pad_modes(modes, n)
        i = input()
        self.mem(write_val=int(i), mode=modes[0])
        return 0

    def output(self, modes):
        n = 1
        modes = self.pad_modes(modes, n)
        print(self.mem(mode=modes[0]))
        return 0

    def jump_if_true(self, modes):
        n = 2
        modes = self.pad_modes(modes, n)
        test = self.mem(mode=modes[0])
        dest = self.mem(mode=modes[1])
        if test:
            self.head = dest
        return 0

    def jump_if_false(self, modes):
        n = 2
        modes = self.pad_modes(modes, n)
        test = self.mem(mode=modes[0])
        dest = self.mem(mode=modes[1])
        if test == 0:
            self.head = dest
        return 0

    def less_than(self, modes):
        n = 3
        modes = self.pad_modes(modes, n)
        op0 = self.mem(mode=modes[0])
        op1 = self.mem(mode=modes[1])
        if op0 < op1:
            self.mem(write_val=1, mode=modes[2])
        else:
            self.mem(write_val=0, mode=modes[2])
        return 0

    def equals(self, modes):
        n = 3
        modes = self.pad_modes(modes, n)
        op0 = self.mem(mode=modes[0])
        op1 = self.mem(mode=modes[1])
        if op0 == op1:
            self.mem(write_val=1, mode=modes[2])
        else:
            self.mem(write_val=0, mode=modes[2])
        return 0

    def adj_rel_base(self, modes):
        n = 1
        modes = self.pad_modes(modes, n)
        op0 = self.mem(mode=modes[0])
        self.rel_base += op0
        return 0

    @staticmethod
    def exit(exit_modes):
        if exit_modes is None:
            exit_modes = []
        return -1

    @staticmethod
    def pad_modes(modes, n):
        return modes + [0] * (n - len(modes))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', dest='source', default='input')
    args = parser.parse_args()
    pc = IntCodeComp(args.source)
    pc.run()
