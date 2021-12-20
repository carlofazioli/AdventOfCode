import itertools

from utilities import load_data


DAY = 1


input_data = load_data(DAY)

# Split input into a list of str:
# input_data = input_data.splitlines()

# Convert to list of int:
input_data = list(map(int, input_data.splitlines()))


if __name__ == '__main__':
    # Part 1:
    diffs = [b-a for a, b in zip(input_data[:-1], input_data[1:])]
    f = lambda x: x > 0
    increases = map(f, diffs)
    answer = sum(increases)

    # Part 2:
    windows = [sum(input_data[i:i+3]) for i in range(len(input_data)-2)]
    diffs = [b-a for a, b in zip(windows[:-1], windows[1:])]
    increases = map(f, diffs)
    answer = sum(increases)
