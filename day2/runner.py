from intcode import IntCodeComputer


# Part 1:
pc = IntCodeComputer(source='test1')
pc.run()
print(pc.tape[0])

pc = IntCodeComputer(source='inputmod')
pc.run()
print(pc.tape[0])


# Part 2
out_target = 19690720
noun_target = 0
verb_target = 0
for noun in range(0, 100):
    for verb in range(0, 100):
        pc = IntCodeComputer(source='input')
        pc.tape[1] = noun
        pc.tape[2] = verb
        pc.run()
        out = pc.tape[0]
        if out == out_target:
            noun_target = noun
            verb_target = verb
print(noun_target)
print(verb_target)
