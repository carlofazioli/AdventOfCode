from datetime import datetime
import itertools
import collections

from utilities import load_data, submit

input_data = load_data(day=12)

# input_data = '''start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end'''

# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))

caves = collections.defaultdict(set)
for line in input_data:
    a, b = line.split('-')
    caves[a].add(b)
    caves[b].add(a)


t1 = datetime.now()
pending = [['start']]
completed = []
while pending:
    path = pending.pop()
    last = path[-1]
    neighbors = caves[path[-1]]
    for n in neighbors:
        if n.islower() and n in path:
            continue
        elif n == 'end':
            completed.append(path + [n])
        else:
            pending.append(path + [n])
answer = len(completed)
print(answer)
dt = datetime.now() - t1
print(dt.total_seconds())

# t1 = datetime.now()
# pending = [['start']]
# completed = []
# while pending:
#     path = pending.pop(0)
#     smalls = [c for c in path if c.islower()]
#     has_small_cave_twice = len(smalls) > len(set(smalls))
#     last = path[-1]
#     neighbors = caves[path[-1]]
#     for n in neighbors:
#         if n == 'end':
#             completed.append(path + [n])
#         elif n == 'start':
#             continue
#         elif n.islower() and n in path and has_small_cave_twice:
#             continue
#         else:
#             pending.append(path + [n])
# answer = len(completed)
# print(answer)
# dt = datetime.now() - t1
# print(dt.total_seconds())


t1 = datetime.now()
answer = 0
state = ('start', {'start'})
queue = collections.deque([state])
while queue:
    loc, prohib = queue.popleft()
    if loc == 'end':
        answer += 1
        continue
    for n in caves[loc]:
        if n not in prohib:
            new_prohib = set(prohib)
            if n.islower():
                new_prohib.add(n)
            queue.append((n, new_prohib))
print(answer)
dt = datetime.now() - t1
print(dt.total_seconds())

t1 = datetime.now()
answer = 0
state = ('start', {'start'}, None)
queue = collections.deque([state])
while queue:
    loc, prohib, twice = queue.popleft()
    if loc == 'end':
        answer += 1
        continue
    for n in caves[loc]:
        if n not in prohib:
            new_prohib = set(prohib)
            if n.islower():
                new_prohib.add(n)
            queue.append((n, new_prohib, None))
        elif twice is None and n != 'start':
            queue.append((n, prohib, n))

print(answer)
dt = datetime.now() - t1
print(dt.total_seconds())