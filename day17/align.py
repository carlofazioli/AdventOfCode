
with open('pic') as f:
    lines = [line.strip('\r\n') for line in f]

dy = len(lines)
dx = len(lines[0])

pic_dict = dict()
for y in range(dy):
    for x in range(dx):
        pic_dict[(x, y)] = lines[y][x]


def intersection(pic, x, y):
    if pic.get((x, y), '.') == '#':
        L = pic.get((x - 1, y), '.') == '#'
        R = pic.get((x + 1, y), '.') == '#'
        U = pic.get((x, y + 1), '.') == '#'
        D = pic.get((x, y - 1), '.') == '#'
        if L and R and U and D:
            return True
    return False

crosses = 0
for y in range(dy):
    for x in range(dx):
        if intersection(pic_dict, x, y):
            print(x, y)
            crosses += x*y

print(crosses)

