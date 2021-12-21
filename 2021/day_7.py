from collections import Counter
from utilities import load_data

YEAR = 2021
DAY = 7
input_data = load_data(year=YEAR, day=DAY)

# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))

crabs = Counter(map(int, input_data[0].split(',')))


def cost_1(a, b):
    return abs(a-b)


def total_1(n):
    c = 0
    for i, p in crabs.items():
        c += p * cost_1(n, i)
    return c


def cost_2(a, b):
    d = abs(b - a)
    return int(d*(d+1)/2)


def total_2(n):
    c = 0
    for i, p in crabs.items():
        c += p * cost_2(n, i)
    return c


part_1 = [total_1(i) for i in range(max(crabs.keys()))]
answer = min(part_1)
print(answer)

part_2 = [total_2(i) for i in range(max(crabs.keys()))]
answer = min(part_2)
print(answer)