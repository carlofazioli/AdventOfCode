def process(memory):

    ins_p = 0

    while True:

        ins = memory[ins_p]

        if ins == 1:
            op1_p = memory[ins_p + 1]
            op2_p = memory[ins_p + 2]
            des_p = memory[ins_p + 3]
            op1 = memory[op1_p]
            op2 = memory[op2_p]
            res = op1 + op2
            memory[des_p] = res
            ins_p += 4

        if ins == 2:
            op1_p = memory[ins_p + 1]
            op2_p = memory[ins_p + 2]
            des_p = memory[ins_p + 3]
            op1 = memory[op1_p]
            op2 = memory[op2_p]
            res = op1 * op2
            memory[des_p] = res
            ins_p += 4

        if ins == 99:
            return memory


if __name__ == '__main__':
    

    # Part 1
    with open('input.txt') as f:
        for line in f:
            program = line
        program = program.split(',')
        program[-1] = program[-1][:-1]
        program = list(map(int,program))
        program_reset = list(program)
        print(process(program))

    # Part 2
    for i in range(100):
        for j in range(100):
            program_test = list(program_reset)
            program_test[1] = i
            program_test[2] = j
            target = 19690720
            if process(program_test)[0] == target:
                print(i, j)
