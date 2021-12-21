from utilities import load_data


YEAR = 2015
DAY = 7
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()

circuit = {'b': 3176}


def and_(a, b):
    try:
        a = int(a)
    except ValueError:
        a = circuit.get(a)
    try:
        b = int(b)
    except ValueError:
        b = circuit.get(b)
    if a is not None and b is not None:
        return a & b


def or_(a, b):
    try:
        a = int(a)
    except ValueError:
        a = circuit.get(a)
    try:
        b = int(b)
    except ValueError:
        b = circuit.get(b)
    if a is not None and b is not None:
        return a | b


def lshift_(a, b):
    try:
        a = int(a)
    except ValueError:
        a = circuit.get(a)
    try:
        b = int(b)
    except ValueError:
        b = circuit.get(b)
    if a is not None and b is not None:
        a = bin(a)[2:].zfill(16)
        for _ in range(b):
            a += '0'
        return int(a[-16:], 2)


def rshift_(a, b):
    try:
        a = int(a)
    except ValueError:
        a = circuit.get(a)
    try:
        b = int(b)
    except ValueError:
        b = circuit.get(b)
    if a is not None and b is not None:
        a = bin(a)[2:].zfill(16)
        for _ in range(b):
            a = '0' + a
        return int(a[:16], 2)


def not_(a):
    try:
        a = int(a)
    except ValueError:
        a = circuit.get(a)
    if a is not None:
        return 65535 ^ a


def nop_(a):
    try:
        a = int(a)
    except ValueError:
        a = circuit.get(a)
    return a


while 'a' not in circuit:
    row = input_data.pop(0)
    instruction, target = row.split(' -> ')
    if 'AND' in instruction:
        op1, op2 = instruction.split(' AND ')
        result = and_(op1, op2)
        if result is not None:
            circuit[target] = result
            continue
    elif 'OR' in instruction:
        op1, op2 = instruction.split(' OR ')
        result = or_(op1, op2)
        if result is not None:
            circuit[target] = result
            continue
    elif 'LSHIFT' in instruction:
        op1, op2 = instruction.split(' LSHIFT ')
        result = lshift_(op1, op2)
        if result is not None:
            circuit[target] = result
            continue
    elif 'RSHIFT' in instruction:
        op1, op2 = instruction.split(' RSHIFT ')
        result = rshift_(op1, op2)
        if result is not None:
            circuit[target] = result
            continue
    elif 'NOT' in instruction:
        op = instruction.split(' ')[1]
        result = not_(op)
        if result is not None:
            circuit[target] = result
            continue
    else:
        if target == 'b':
            continue
        op = instruction
        result = nop_(op)
        if result is not None:
            circuit[target] = result
            continue
    input_data.append(row)

answer = circuit['a']
print(answer)