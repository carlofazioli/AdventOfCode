import itertools
import collections
from pprint import pprint

from utilities import load_data, submit

input_data = load_data(day=8)


# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))

answer = None

count = 0
for line in input_data:
    a, b = line.split(' | ')
    b = b.split(' ')
    for item in b:
        if len(item) in [2, 3, 4, 7]:
            count += 1
answer = count

answer = 0
for line in input_data:
    pattern, output = line.split(' | ')
    pattern = [''.join(sorted(s)) for s in pattern.split(' ')]
    output = [''.join(sorted(s)) for s in output.split(' ')]
    pattern.sort(key=len)
    mapping = {
        pattern[0]: 1,
        pattern[1]: 7,
        pattern[2]: 4,
        pattern[-1]: 8
    }
    for X in pattern[6:9]:
        if (set(pattern[-1]) - set(X)) < set(pattern[0]):
            mapping[X] = 6
            six = set(X)
        elif (set(pattern[-1]) - set(X)) < set(pattern[2]):
            mapping[X] = 0
        else:
            mapping[X] = 9
    for X in pattern[3:6]:
        if not (set(pattern[-1]) - set(X)).intersection(set(pattern[0])):
            mapping[X] = 3
        elif (six.intersection(set(X))).intersection(set(pattern[0])):
            mapping[X] = 5
        else:
            mapping[X] = 2
    out = ''.join(str(mapping[s]) for s in output)
    answer += int(out)



part = 2
print(answer)
# submit(answer, part)