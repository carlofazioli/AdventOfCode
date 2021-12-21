from utilities import load_data

YEAR = 2021
DAY = 2
input_data = load_data(year=YEAR, day=DAY)

# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data.splitlines()))


def main():
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in input_data:
        a, x = instruction.split(' ')
        x = int(x)
        if a == 'forward':
            horizontal += x
            depth += aim*x
        if a == 'down':
            aim += x
        if a == 'up':
            aim -= x

    answer = horizontal*depth
    print(answer)


if __name__ == '__main__':
    main()