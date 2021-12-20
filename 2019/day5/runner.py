from intcode import IntCodeComputer


# Part 1: (STDIN/STDOUT mode)
pc = IntCodeComputer(source='input')
pc.run()

# Part 1: (Programmatic IO mode)
pc = IntCodeComputer(source='input', buffered=True)
result, flag = pc.run(1)
print(result, flag)


# Part 2: (STDIN/STDOUT mode)
pc = IntCodeComputer(source='input')
pc.run()

# Part 2: (Programmatic IO mode)
pc = IntCodeComputer(source='input', buffered=True)
result, flag = pc.run(5)
print(result, flag)
