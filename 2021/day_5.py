import itertools

from utilities import load_data, submit

input_data = load_data()


# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))


floor_map = {}


def p():
    for y in range(10):
        for x in range(10):
            print(floor_map.get((x, y), '0'), end='')
        print()


for line in input_data:
    start, end = line.split(' -> ')
    x0, y0 = list(map(int, start.split(',')))
    x1, y1 = list(map(int, end.split(',')))
    dx = 1 if x1 > x0 else 0 if x1 == x0 else -1
    dy = 1 if y1 > y0 else 0 if y1 == y0 else -1
    loc = (x0, y0)
    while True:
        if loc in floor_map:
            floor_map[loc] += 1
        else:
            floor_map[loc] = 1
        loc = (loc[0] + dx, loc[1] + dy)
        if loc == (x1, y1):
            if loc in floor_map:
                floor_map[loc] += 1
            else:
                floor_map[loc] = 1
            break

danger = 0
for loc, val in floor_map.items():
    if val >= 2:
        danger += 1





answer = danger
print(answer)
# submit(answer, part)

