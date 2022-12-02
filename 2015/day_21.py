from math import inf
import itertools
from utilities import load_data


YEAR = 2015
DAY = 21
input_data = load_data(year=YEAR, day=DAY)

weapons_string = '''Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0'''

armor_string = '''Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5'''

rings_string = '''Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3'''

weapons = []
weapons_string = weapons_string.splitlines()
for w in weapons_string:
    w = w.split()
    weapons.append(list(map(int, w[1:])))

armor = [[0, 0, 0]]
armor_string = armor_string.splitlines()
for a in armor_string:
    a = a.split()
    armor.append(list(map(int, a[1:])))

rings = []
rings_string = rings_string.splitlines()
for r in rings_string:
    r = r.split()
    rings.append(list(map(int, r[1:])))

combos = []
for count in range(2, len(rings)+1):
    for subset in itertools.combinations(rings, count):
        c, d, a = 0, 0, 0
        for r in subset:
            c += r[0]
            d += r[1]
            a += r[2]
        combos.append([c, d, a])

rings += combos
rings.append([0, 0, 0])
rings.sort(key=lambda r: r[0])



def player_wins(boss, player):
    pd = max(player[1] - boss[2], 1)
    bd = max(boss[1] - player[2], 1)
    while True:
        boss[0] -= pd
        if boss[0] <= 0:
            return True
        player[0] -= bd
        if player[0] <= 0:
            return False


def solve():
    min_cost = inf
    max_cost = 0
    for w in weapons:
        for a in armor:
            for rs in rings:
                boss = [104, 8, 1]
                player = [100, 0, 0]
                cost = w[0] + a[0] + rs[0]
                if cost == 10:
                    print(f'{cost=}, {w=}, {a=}, {rs=}')
                player[1] += w[1] + a[1] + rs[1]
                player[2] += w[2] + a[2] + rs[2]
                if player_wins(boss, player):
                    min_cost = min(min_cost, cost)
                else:
                    max_cost = max(max_cost, cost)
    return min_cost, max_cost


lo, hi = solve()
print(lo)
print(hi)
