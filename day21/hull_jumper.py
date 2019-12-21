from intcode import IntCodeComputer


def convert_to_ascii(s):
    return list(map(ord, list(s)))


def parse_result(r):
    out = []
    for v in r[0]:
        try:
            ch = chr(v)
            out.append(ch)
        except:
            print('Big value: ', v)
            continue
    print(r[1])
    print(''.join(out))


pc_1 = IntCodeComputer(source='input', buffered=True)

program_1 = [
    'NOT A T\n',
    'OR T J\n',
    'NOT B T\n',
    'OR T J\n',
    'NOT C T\n',
    'OR T J\n',  # At this point, if A, B, or C is FALSE, J is TRUE.
    'AND D J\n',  # If the destination D is TRUE (safe), jump now.
    'WALK\n',
]

result = pc_1.run()
parse_result(result)


instruction = 0
while result[1] == 'PENDING':
    print('Programming instruction: ', program_1[instruction])
    inp = convert_to_ascii(program_1[instruction])
    result = pc_1.run(inp)
    parse_result(result)
    instruction += 1

# Part 2:
pc_2 = IntCodeComputer(source='input', buffered=True)

program_2 = [
    'NOT A T\n',
    'OR T J\n',
    'NOT B T\n',
    'OR T J\n',
    'NOT C T\n',
    'OR T J\n',  # These ^^ instructions identify the need to jump, and store it in J.
                 # At this point, if A, B, or C is FALSE, J is TRUE; else J is FALSE

    'OR J T\n',  # This instruction syncs T and J.  At this point, T=J

    'AND D J\n',
    'AND E J\n',  # These instructions identify whether E is safe to advance to after landing at D; stores in J.
                  # At this point if J was TRUE and D=E=TRUE (safe), then J is TRUE; else J is FALSE

    'AND D T\n',
    'AND H T\n',  # These indicate that H will be safe to jump to immediately after landing at D; stores in T.
                  # At this point, if T was TRUE and D=H=TRUE (safe), then T is TRUE; else T is FALSE

    'OR T J\n',  # If either T or J is TRUE (safe), jump!

    'RUN\n',
]

result = pc_2.run()
parse_result(result)

instruction = 0
while result[1] == 'PENDING':
    print('Programming instruction: ', program_2[instruction])
    inp = convert_to_ascii(program_2[instruction])
    result = pc_2.run(inp)
    parse_result(result)
    instruction += 1

