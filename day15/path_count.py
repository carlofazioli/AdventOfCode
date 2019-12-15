from day15.runner import Map


with open('map') as f:
    map_str = f.read()

steps = 1
for ch in map_str:
    if ch == '+':
        steps += 1

print(steps)

with open('map_full') as f:
    lines = [line.strip('\r\n') for line in f]

dx = len(lines[0])
dy = len(lines)

map_dict = dict()
for y in range(dy):
    for x in range(dx):
        ch = lines[y][x]
        if ch != 'S':
            map_dict[(x, y)] = ch
        else:
            map_dict[(x, y)] = ' '

m = Map()
m.map = map_dict

m.draw()


def map_full(map, dx, dy):
    full = True
    for x in range(dx):
        for y in range(dy):
            if map.get((x, y), '#') == ' ':
                full = False
    return full


def adjacent_o(map, x, y):
    adj = False
    if map.get((x, y), '#') == ' ':
        up = map.get((x, y + 1), '#') == 'O'
        down = map.get((x, y - 1), '#') == 'O'
        left = map.get((x - 1, y), '#') == 'O'
        right = map.get((x + 1, y), '#') == 'O'
        adj = up or down or left or right
    return adj

updates = dict()
minutes = 0

while not map_full(m.map, dx, dy):
    for y in range(dy):
        for x in range(dx):
            if adjacent_o(m.map, x, y):
                updates[(x, y)] = True

    for y in range(dy):
        for x in range(dx):
            if updates.get((x, y)):
                m.map[(x, y)] = 'O'

    m.draw()
    minutes += 1

print(minutes)
