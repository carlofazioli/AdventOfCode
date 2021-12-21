from collections import defaultdict
from utilities import load_data


YEAR = 2015
DAY = 9
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()

graph = defaultdict(list)
longest = -1
shortest = 1e9
ends = []
for leg in input_data:
    rte, d = leg.split(' = ')
    a, b = rte.split(' to ')
    d = int(d)
    if d > longest:
        longest = d
        ends = (a, b)
    if d < shortest:
        shortest = d
        part_2_start = a
    graph[a].append((b, d))
    graph[b].append((a, d))

# answer = 0
# route = [ends[0]]
# while len(route) < 8:
#     dlist = graph[route[-1]]
#     dlist.sort(key=lambda x:x[1])
#     p = dlist.pop(0)
#     while p[0] in route:
#         p = dlist.pop(0)
#     route.append(p[0])
#     answer += p[1]
# print(answer)

answer = 0
route = [part_2_start]
while len(route) < 8:
    dlist = graph[route[-1]]
    dlist.sort(key=lambda x:x[1])
    p = dlist.pop()
    while p[0] in route:
        p = dlist.pop()
    route.append(p[0])
    answer += p[1]
print(answer)