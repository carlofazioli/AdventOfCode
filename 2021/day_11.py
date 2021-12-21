from utilities import load_data


YEAR = 2021
DAY = 11
input_data = load_data(year=YEAR, day=DAY)

# Split input into a list of str:
input_data = input_data.splitlines()
input_data = [list(map(int, row)) for row in input_data]

octs = {}
for y in range(10):
    for x in range(10):
        octs[(x, y)] = input_data[y][x]


def p():
    for y in range(10):
        for x in range(10):
            print(octs[(x, y)], end='')
        print()
    print()

flashes = 0
for _ in range(10000):
    flashed = []
    for loc, octopus in octs.items():
        octs[loc] += 1
    while max(octs.values()) > 9:
        for loc, octopus in octs.items():
            x, y = loc
            if octopus > 9:
                octs[loc] = 0
                flashes += 1
                flashed.append(loc)
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        if 0 > x+dx or x+dx > 9 or 0 > y+dy or y+dy > 9:
                            continue
                        octs[(x+dx, y+dy)] += 1
    for loc in flashed:
        octs[loc] = 0
    if len(flashed) == 100:
        print(_)
        input()
