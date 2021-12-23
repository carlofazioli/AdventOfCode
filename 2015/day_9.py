import itertools
from collections import defaultdict
from utilities import load_data


YEAR = 2015
DAY = 9
input_data = load_data(year=YEAR, day=DAY)

# input_data = '''London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# '''

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
for route in itertools.permutations(graph.keys()):
    s = 0
    for i in range(len(route)-1):
        dlist = graph[route[i]]
        for loc, d in dlist:
            if loc == route[i+1]:
                s += d
    answer = max(answer, s)

print(answer)
