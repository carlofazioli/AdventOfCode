from utilities import load_data


YEAR = 2015
DAY = 23
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()

reg = {
    'a': 1,
    'b': 0
}
ins_p = 0

while ins_p < len(input_data):
    instruction = input_data[ins_p]
    instruction = instruction.replace(',', '')
    instruction = instruction.split()
    if instruction[0] == 'hlf':
        reg[instruction[1]] //= 2
        ins_p += 1
    elif instruction[0] == 'tpl':
        reg[instruction[1]] *= 3
        ins_p += 1
    elif instruction[0] == 'inc':
        reg[instruction[1]] += 1
        ins_p += 1
    elif instruction[0] == 'jmp':
        ins_p += int(instruction[1])
    elif instruction[0] == 'jie':
        if reg[instruction[1]] % 2 == 0:
            ins_p += int(instruction[2])
        else:
            ins_p += 1
    elif instruction[0] == 'jio':
        if reg[instruction[1]] == 1:
            ins_p += int(instruction[2])
        else:
            ins_p += 1

answer = reg['b']
print(answer)