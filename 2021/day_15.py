from math import inf
import heapq

from utilities import load_data


YEAR = 2021
DAY = 15
input_data = load_data(year=YEAR, day=DAY)

# input_data = '''1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581'''

# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))
width = len(input_data[0])
floor_plan = {}
for y in range(width):
    for x in range(width):
        floor_plan[(x, y)] = int(input_data[y][x])

tiling = 5
source = (0, 0)
target = (tiling*width-1, tiling*width-1)
dist = {}
queue = [(0, source)]
while queue:
    d, loc = heapq.heappop(queue)
    if not (0 <= loc[0] < tiling*width and 0 <= loc[1] < tiling*width):
        continue
    i = loc[0] % width
    j = loc[1] % width
    fp = floor_plan[(i, j)]
    i = loc[0] // width
    j = loc[1] // width
    fp += i + j
    while fp > 9:
        fp -= 9
    cost = d + fp
    if dist.get(loc, inf) > cost:
        dist[loc] = cost
    else:
        continue
    if loc == target:
        break
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        new_loc = (loc[0]+dx, loc[1]+dy)
        heapq.heappush(queue, (dist[loc], new_loc))
print(dist[target] - floor_plan[source])
