from utilities import load_data


YEAR = 2021
DAY = 16
input_data = load_data(year=YEAR, day=DAY)

# input_data = '9C0141080250320F1802104A08'
# Split input into a list of str:
# input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))

bits = ''
for ch in input_data:
    v = bin(int(ch, 16))[2:].zfill(4)
    bits += v


def parse(bits):
    if len(bits) < 8:
        return 0, ''
    vvv, bits = bits[:3], bits[3:]
    ttt, bits = bits[:3], bits[3:]
    if ttt == '100':
        # Literal
        val = ''
        i, data, bits = bits[0], bits[1:5], bits[5:]
        while i == '1':
            val += data
            i, data, bits = bits[0], bits[1:5], bits[5:]
        val += data
        return int(val, 2), bits
    else:
        length_type, bits = bits[0], bits[1:]
        literals = []
        if length_type == '0':
            subpackets_length, bits = int(bits[:15], 2), bits[15:]
            subpackets, bits = bits[:subpackets_length], bits[subpackets_length:]
            while subpackets:
                val, subpackets = parse(subpackets)
                literals.append(val)
        elif length_type == '1':
            subpackets_count, bits = int(bits[:11], 2), bits[11:]
            for _ in range(subpackets_count):
                val, bits = parse(bits)
                literals.append(val)
        val = None
        ttt = int(ttt, 2)
        if ttt == 0:
            val = sum(literals)
        if ttt == 1:
            val = 1
            for literal in literals:
                val *= literal
        if ttt == 2:
            val = min(literals)
        if ttt == 3:
            val = max(literals)
        if ttt == 5:
            val = int(literals[0] > literals[1])
        if ttt == 6:
            val = int(literals[0] < literals[1])
        if ttt == 7:
            val = int(literals[0] == literals[1])
        return val, bits


answer, leftovers = parse(bits)
print(answer)