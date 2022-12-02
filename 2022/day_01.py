from pathlib import Path

input_file = '/home/carlo/AdventOfCode/2022/input_data/day_01.txt'
with open(input_file, 'r') as f:
    input_data = f.read().strip()


input_data = input_data.split('\n\n')

m = -1
idx = -1
for i, s in enumerate(input_data):
    s = s.split()
    s = map(int, s)
    s = sum(s)
    if s > m:
        m = s
        idx = i

print(m)

final = 0
for n in range(0,3):
    m = -1
    idx = -1
    for i, s in enumerate(input_data):
        s = s.split()
        s = map(int, s)
        s = sum(s)
        if s > m:
            m = s
            idx = i
    final += m
    input_data[idx]=''

print(final)
