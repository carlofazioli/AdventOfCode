from utilities import load_data


YEAR = 2016
DAY = 8
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()

h = 6
w = 50


def rect(axbstr, screen):
    a, b = axbstr.split('x')
    a = int(a)
    b = int(b)
    for y in range(b):
        for x in range(a):
            screen.add((x, y))
    return screen


def rotate_row(spec, screen):
    row = int(spec[0].split('=')[1])
    shift = int(spec[2])
    new_row = set()
    for x in range(w):
        if (x, row) in screen:
            new_row.add(((x+shift) % w, row))
            screen.discard((x, row))
    return screen.union(new_row)


def rotate_col(spec, screen):
    col = int(spec[0].split('=')[1])
    shift = int(spec[2])
    new_col = set()
    for y in range(h):
        if (col, y) in screen:
            new_col.add((col, (y+shift) % h))
            screen.discard((col, y))
    return screen.union(new_col)


screen = set()
for instruction in input_data:
    instruction = instruction.split()
    if instruction[0] == 'rect':
        screen = rect(instruction[1], screen)
    if instruction[0] == 'rotate':
        if instruction[1] == 'row':
            screen = rotate_row(instruction[2:], screen)
        else:
            screen = rotate_col(instruction[2:], screen)

answer = len(screen)
print(answer)

for y in range(h):
    row = ''
    for x in range(w):
        row += '#' if (x, y) in screen else ' '
    print(row)
