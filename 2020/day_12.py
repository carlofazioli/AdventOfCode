import math
import utilities


instructions = utilities.input_to_list('day_12.txt')


def parse_instruction(ins, pos, heading, debug=False):
    action = ins[0]
    val = int(ins[1:])
    if debug:
        print('Step:')
        print('pos:', pos)
        print('hdg:', heading)
        print('ins:', ins)
        print('act:', action)
        print('val:', val)
        print()
    if action == 'N':
        pos[1] += val
    if action == 'S':
        pos[1] -= val
    if action == 'E':
        pos[0] += val
    if action == 'W':
        pos[0] -= val
    if action in 'LR':
        theta = (1-2*(action == 'R'))*math.pi*val/180
        c = int(math.cos(theta))
        s = int(math.sin(theta))
        heading = [c*heading[0] - s*heading[1], s*heading[0] + c*heading[1]]
    if action == 'F':
        pos[0] += val*heading[0]
        pos[1] += val*heading[1]
    if debug:
        print('Result')
        print('pos:', pos)
        print('hdg:', heading)
        print('\n\n')
    return pos, heading


pos = [0, 0]
heading = [1, 0]

for instruction in instructions:
    pos, heading = parse_instruction(instruction, pos, heading, debug=False)

print(pos)


def parse_ins_2(ins, pos, offset):
    action = ins[0]
    val = int(ins[1:])
    if action == 'N':
        offset[1] += val
    if action == 'S':
        offset[1] -= val
    if action == 'E':
        offset[0] += val
    if action == 'W':
        offset[0] -= val
    if action in 'LR':
        theta = (1-2*(action == 'R'))*math.pi*val/180
        c = int(math.cos(theta))
        s = int(math.sin(theta))
        offset = [c*offset[0] - s*offset[1], s*offset[0] + c*offset[1]]
    if action == 'F':
        pos[0] += val*offset[0]
        pos[1] += val*offset[1]
    return pos, offset


pos = [0, 0]
offset = [10, 1]
for instruction in instructions:
    pos, offset = parse_ins_2(instruction, pos, offset)

print(pos)