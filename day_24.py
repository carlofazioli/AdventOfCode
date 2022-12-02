import functools
import itertools
from math import inf
from copy import deepcopy
from utilities import load_data


YEAR = 2015
DAY = 24
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()
input_data = list(map(int, input_data))


input_data.sort(reverse=True)


def qe(bin):
    prod = 1
    for val in bin:
        prod *= val
    return prod


part_1 = inf
for subset_size in range(1, 7):
    for subset in itertools.combinations(input_data, subset_size):
        if sum(subset) == sum(input_data)//3:
            part_1 = min(part_1, qe(subset))

print(part_1)


part_2 = inf
for subset_size in range(1, 7):
    for subset in itertools.combinations(input_data, subset_size):
        if sum(subset) == sum(input_data)//4:
            part_2 = min(part_2, qe(subset))

print(part_2)
