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


pc = IntCodeComputer(source='input', buffered=True)

result = pc.run()
parse_result(result)

while result[1] == 'PENDING':
    inp_raw = input()
    inp = convert_to_ascii(inp_raw + '\n')
    result = pc.run(inp)
    parse_result(result)

