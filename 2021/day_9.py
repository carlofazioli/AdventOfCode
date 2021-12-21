import collections
from math import inf
from utilities import load_data


YEAR = 2021
DAY = 9
input_data = load_data(year=YEAR, day=DAY)


# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))

heightmap = collections.defaultdict(lambda: inf)
for y, row in enumerate(input_data):
    for x, h in enumerate(row):
        heightmap[(x, y)] = int(h)

minima = []
answer = 0
for loc, val in heightmap.items():
    x, y = loc
    R = heightmap.get((x+1, y), inf)
    U = heightmap.get((x, y+1), inf)
    L = heightmap.get((x-1, y), inf)
    D = heightmap.get((x, y-1), inf)
    if all(map(lambda a: val < a, [R, U, L, D])):
        answer += val + 1
        minima.append(loc)
print(answer)


basins = []
for m in minima:
    basin = set()
    queue = [m]
    count = 0
    while queue:
        x, y = queue.pop()
        if heightmap.get((x, y), inf) < 9:
            basin.add((x, y))
        R = (x+1, y)
        U = (x, y+1)
        L = (x-1, y)
        D = (x, y-1)
        for neighbor in [R, U, L, D]:
            if heightmap.get(neighbor, inf) < 9 and neighbor not in basin:
                queue.append(neighbor)
    basins.append(len(basin))

basins.sort()
u, v, w = basins[-3:]
answer = u*v*w
print(answer)