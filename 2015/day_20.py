from math import sqrt, floor
from utilities import load_data


YEAR = 2015
DAY = 20
input_data = 29000000
presents = input_data


def sum_factors(n):
    s = 0
    sqrt_n = sqrt(n)
    for i in range(1, floor(sqrt_n)+1):
        if n % i == 0:
            s += i
            s += n//i
    s -= int(sqrt_n) if n % sqrt_n == 0 else 0
    return s*10


def sum_factors_2(n):
    s = 0
    sqrt_n = sqrt(n)
    for i in range(1, floor(sqrt_n)+1):
        if n % i == 0:
            s += i if n//i <= 50 else 0
            s += n//i if i <= 50 else 0
    if sqrt_n <= 50 and n % sqrt_n == 0:
        s -= int(sqrt_n)
    return s*11


house = 8
while sum_factors(house) < presents:
    house += 1
print(house)

while sum_factors_2(house) < presents:
    house += 1
print(house)