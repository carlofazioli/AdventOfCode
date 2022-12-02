from utilities import load_data


YEAR = 2015
DAY = 18
input_data = load_data(year=YEAR, day=DAY)

# input_data = '''.#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..'''

input_data = input_data.splitlines()


h = len(input_data)
w = len(input_data[0])
sims = 100

on = set()
for y in range(h):
    for x in range(w):
        if input_data[y][x] == '#':
            on.add((x, y))

on.add((0, 0))
on.add((0, h-1))
on.add((w-1, 0))
on.add((w-1, h-1))

for _ in range(sims):
    new_on = set()
    new_off = set()
    for y in range(h):
        for x in range(w):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if (x+dx, y+dy) in on:
                        count += 1
            if (x, y) in on:
                if count < 2 or count > 3:
                    new_off.add((x, y))
            elif count == 3:
                new_on.add((x, y))
    for loc in new_on:
        on.add(loc)
    for loc in new_off:
        on.discard(loc)

    on.add((0, 0))
    on.add((0, h-1))
    on.add((w-1, 0))
    on.add((w-1, h-1))

    # for y in range(h):
    #     s = ''
    #     for x in range(w):
    #         s += '#' if (x, y) in on else ' '
    #     print(s)
    # print()
    # print()

answer = len(on)
print(answer)
