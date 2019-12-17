from numpy import gcd, lcm


class Signal:
    def __init__(self,
                 pattern_source=None,
                 pattern_reps=1,
                 length=None,):
        # If no source is given, the data dict will be empty but a signal length can be specified.
        #
        # If an input source is given (e.g. a file), then a number of pattern reps is associated
        # and a length is inferred.

        if pattern_source is None:
            self.pattern_length = length
            self.length = length
            self.pattern = dict()
        else:
            sig_list = []
            if isinstance(pattern_source, str):
                with open(pattern_source) as f:
                    sig_str = f.readline()
                sig_list = list(map(int, list(sig_str.rstrip('\r\n'))))
            if isinstance(pattern_source, list):
                sig_list = pattern_source
            self.pattern_length = len(sig_list)
            self.length = len(sig_list) * pattern_reps
            # Build dictionary:
            self.pattern = dict()
            for i, v in enumerate(sig_list):
                if v != 0:
                    self.pattern[i] = v

    def __getitem__(self, item):
        item %= self.length
        return self.pattern.get(item, 0)

    def __setitem__(self, key, value):
        if value != 0:
            self.pattern[key] = value

    def __len__(self):
        return self.length


class Processor:
    def __init__(self,
                 data,
                 use_offset=False):
        self.data = data
        self.period = self.data.pattern_length
        self.kernel = Signal([0, 1, 0, -1])
        if use_offset:
            self.get_offset()
        else:
            self.offset = 0

    def get_output_digit(self, d):
        kernel_period = 4 * (d+1)
        read_length = lcm(self.period, kernel_period)
        full_reads = self.data.length // read_length
        frag_reads = self.data.length % read_length
        out = 0
        if 1 <= full_reads <= 9:
            for j in range(min(read_length, self.data.length)):
                out += self.data[j] * self.kernel[(j + 1) // (d + 1)]
        for j in range(frag_reads):
            out += self.data[j] * self.kernel[(j + 1) // (d + 1)]
        return abs(out) % 10

    def process_phase(self):
        output = Signal(length=self.data.length)
        for i in range(len(self.data)):
            output[i] = self.get_output_digit(i)
        self.data = output

    def get_offset(self):
        offset = []
        for i in range(7):
            offset.append(self.data[i])
        self.offset = int(''.join(list(map(str, offset))))

    def display(self):
        output = []
        for i in range(8):
            output.append(self.data[i + self.offset])
        return output


# Part 1:
n_phases = 100
sig = Signal(pattern_source='test5', pattern_reps=10000)
fft = Processor(data=sig, use_offset=True)
for p in range(n_phases):
    print('Running phase: ', p)
    fft.process_phase()
print(fft.display())



#
# sig = Signal('test3')
#
# for k in range(n_phases):
#     print('Running phase {}'.format(k))
#     sig = process(sig)
#
# offset = get_offset(sig_pattern)
# print(sig[offset:offset + 8])
#
input()