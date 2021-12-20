import itertools
import collections
from math import inf

from utilities import load_data, submit

input_data = load_data(day=17)
# input_data = 'target area: x=20..30, y=-10..-5'
input_data = input_data.split(',')
x_min, x_max = list(map(int, input_data[0].split('=')[1].split('..')))
y_min, y_max = list(map(int, input_data[1].split('=')[1].split('..')))


def compute_acme(vel):
    dx, dy = vel
    x = [d*(d+1)//2 for d in range(dx)]
    y = [d*(d+1)//2 for d in range(dy)]


def step(loc, vel):
    x, y = loc
    dx, dy = vel
    x += dx
    y += dy
    if dx > 0:
        dx -= 1
    elif dx < 0:
        dx += 1
    dy -= 1
    return (x, y), (dx, dy)


def hit(loc):
    return x_min <= loc[0] <= x_max and y_min <= loc[1] <= y_max


def simulate(vel):
    x, y = (0, 0)
    dx, dy = vel
    acme = dy*(dy+1)//2
    while x < x_max and y >= y_min:
        loc, vel = step((x, y), (dx, dy))
        x, y = loc
        dx, dy = vel
        if hit(loc):
            return acme
    return -inf


def solve():
    answer = 0
    acmes = []
    for dy in range(-1000, 1000):
        for dx in range(126):
            acme = simulate((dx, dy))
            if acme > -inf:
                acmes.append(acme)
    return acmes

acmes = solve()
top = max(acmes)
count = len(acmes)