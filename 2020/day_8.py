import utilities


boot_code = utilities.input_to_list('day_8.txt')


def parse_instruction(i, ptr, accumulator):
    op, arg = i.split(' ')
    if op == 'acc':
        accumulator += int(arg)
        ptr += 1
    if op == 'jmp':
        ptr += int(arg)
    if op == 'nop':
        ptr += 1
    return ptr, accumulator


def run(code, decorrupt=None):
    ptr = 0
    accumulator = 0
    executed_instructions = []
    while True:
        if ptr in executed_instructions:
            status = 'looped'
            break
        if ptr == len(code):
            status = 'terminated'
            break
        executed_instructions.append(ptr)
        next_instruction = code[ptr]
        if ptr == decorrupt:
            if 'jmp' in next_instruction:
                next_instruction = next_instruction.replace('jmp', 'nop')
            elif 'nop' in next_instruction:
                next_instruction = next_instruction.replace('nop', 'jmp')
        ptr, accumulator = parse_instruction(next_instruction, ptr, accumulator)
    return accumulator, status


print(run(boot_code))
for i in range(len(boot_code)):
    out = run(boot_code, decorrupt=i)
    if out[1] == 'terminated':
        print(out[0])