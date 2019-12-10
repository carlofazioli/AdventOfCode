import argparse


class IntCodeComputer:
    def __init__(self,
                 source=None,
                 debug=False,
                 save=False):
        if source:
            self.load_memory(source)
        else:
            self.mem = None
        self.head = 0
        self.relative_base = 0
        self.opcodes = {
            1: {'exe': self.add,
                'n': 3},
            2: {'exe': self.mult,
                'n': 3},
            3: {'exe': self.input,
                'n': 1},
            4: {'exe': self.output,
                'n': 1},
            5: {'exe': self.jump_if_true,
                'n': 2},
            6: {'exe': self.jump_if_false,
                'n': 2},
            7: {'exe': self.less_than,
                'n': 3},
            8: {'exe': self.equals,
                'n': 3},
            9: {'exe': self.adj_rel_base,
                'n': 1},
            99: {'exe': self.exit,
                 'n': 0},
        }
        self.debug = debug
        self.save = save

    # Main function:
    def run(self, source=None):
        self.load_memory(source=source)
        while True:
            # Get opcode and modes:
            exe, modes = self.parse_opcode()
            # Execute op:
            adv = exe(modes=modes)
            if adv < 0:
                break
            # Advance the head:
            self.head += adv
        self.head = 0

    # Disk IO:
    def load_memory(self, source=None):
        if isinstance(source, str):
            with open(source) as f:
                mem_str = f.readline()
            mem_str.rstrip('\r\n')
            self.mem = list(map(int, mem_str.split(',')))
        if isinstance(source, list):
            self.mem = source

    # Basic memory function:
    def read(self, loc, mode=0):
        if mode == 2:
            # Make sure the mem tape is long enough:
            relloc = loc + self.relative_base
            if relloc > len(self.mem):
                self.mem += [0] * (relloc - len(self.mem) + 1)
            return self.mem[relloc]
        if mode == 1:
            return self.mem[loc]
        else:
            return self.mem[self.mem[loc]]

    def write(self, loc, val, mode=0):
        if loc > len(self.mem):
            self.mem += [0] * (loc - len(self.mem) + 1)
        if self.mem[loc] > len(self.mem):
            self.mem += [0] * (self.mem[loc] - len(self.mem) + 1)
        if mode == 2:
            relloc = loc + self.relative_base
            if relloc > len(self.mem):
                self.mem += [0] * (relloc - len(self.mem) + 1)
            self.mem[self.mem[relloc]] = val
        else:
            self.mem[self.mem[loc]] = val

    def parse_opcode(self):
        op_raw = self.read(self.head, mode=1)
        # Zero-pad the opcode to be at least 2 digits:
        op_s = str(op_raw).zfill(2)
        # Extract the last 2 digits:
        op = int(op_s[-2:])
        exe = self.opcodes[op]['exe']
        n = self.opcodes[op]['n']
        # Extract the modes:
        opcode_s = str(op_raw).zfill(2 + n)
        modes = list(map(int, list(str(opcode_s)[:n][::-1])))
        return exe, modes

    # OpCode Definitions:
    def add(self, modes=None):
        if modes is None:
            modes = [0, 0, 0]
        op0 = self.read(self.head + 1, modes[0])
        op1 = self.read(self.head + 2, modes[1])
        self.write(self.head + 3, op0 + op1, modes[2])
        return len(modes) + 1

    def mult(self, modes=None):
        if modes is None:
            modes = [0, 0, 0]
        op0 = self.read(self.head + 1, modes[0])
        op1 = self.read(self.head + 2, modes[1])
        self.write(self.head + 3, op0*op1, modes[2])
        return len(modes) + 1

    def exit(self, modes=None):
        return -1

    def input(self, modes=None):
        if modes is None:
            modes = [0]
        i = input()
        self.write(self.head + 1, int(i), modes[0])
        return len(modes) + 1

    def output(self, modes=None):
        if modes is None:
            modes = [0]
        print(self.read(self.head + 1, modes[0]))
        return len(modes) + 1

    def jump_if_true(self, modes=None):
        if modes is None:
            modes = [0, 0]
        if self.read(self.head + 1, modes[0]):
            self.head = self.read(self.head + 2, modes[1])
            return 0
        return len(modes) + 1

    def jump_if_false(self, modes=None):
        if modes is None:
            modes = [0, 0]
        if self.read(self.head + 1, modes[0]) == 0:
            self.head = self.read(self.head + 2, modes[1])
            return 0
        return len(modes) + 1

    def less_than(self, modes=None):
        if modes is None:
            modes = [0, 0, 0]
        op0 = self.read(self.head + 1, modes[0])
        op1 = self.read(self.head + 2, modes[1])
        if op0 < op1:
            self.write(self.head + 3, 1, modes[2])
        else:
            self.write(self.head + 3, 0, modes[2])
        return len(modes) + 1

    def equals(self, modes=None):
        if modes is None:
            modes = [0, 0, 0]
        op0 = self.read(self.head + 1, modes[0])
        op1 = self.read(self.head + 2, modes[1])
        if op0 == op1:
            self.write(self.head + 3, 1, modes[2])
        else:
            self.write(self.head + 3, 0, modes[2])
        return len(modes) + 1

    def adj_rel_base(self, modes=None):
        if modes is None:
            modes = [0]
        op0 = self.read(self.head + 1, modes[0])
        self.relative_base += op0
        return len(modes) + 1

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    args = parser.parse_args()

    pc = IntCodeComputer()
    pc.run(args.source)
