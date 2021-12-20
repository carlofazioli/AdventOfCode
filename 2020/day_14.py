import utilities


instructions = utilities.input_to_list('day_14.txt')


class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.mem = dict()
        self.mask = None

    def run(self):
        for instruction in self.instructions:
            self.parse_instruction(instruction)

    def parse_instruction(self, ins):
        if ins[:4] == 'mask':
            self.mask = ins[7:]
        if ins[:3] == 'mem':
            loc, _, val = ins.split(' ')
            loc = int(loc[4:-1])
            val = bin(int(val))[2:].zfill(36)
            self.mem[loc] = self.mask_val(val)

    def mask_val(self, val):
        val = list(val)
        for i, m in enumerate(self.mask):
            if m == 'X':
                continue
            if m == '1':
                val[i] = '1'
            if m == '0':
                val[i] = '0'
        return ''.join(val)

    def sum_mem(self):
        s = 0
        for val in self.mem.values():
            s += int(val, 2)
        return s


p = Program(instructions)
p.run()
print(p.sum_mem())


class ProgramV2(Program):
    def parse_instruction(self, ins):
        if ins[:4] == 'mask':
            self.mask = ins[7:]
        if ins[:3] == 'mem':
            loc, _, val = ins.split(' ')
            loc = bin(int(loc[4:-1]))[2:].zfill(36)
            val = bin(int(val))[2:].zfill(36)
            loc = self.mask_mem(loc)
            self.update_mem(loc, val)

    def mask_mem(self, loc):
        loc = list(loc)
        for i, m in enumerate(self.mask):
            if m == 'X':
                loc[i] = 'X'
            if m == '0':
                continue
            if m == '1':
                loc[i] = '1'
        return ''.join(loc)

    def update_mem(self, loc, val):
        n = loc.count('X')
        loc = loc.replace('X', '{}')
        for i in range(2**n):
            b = list(bin(i)[2:].zfill(n))
            self.mem[loc.format(*b)] = val


p2 = ProgramV2(instructions)
p2.run()
print(p2.sum_mem())