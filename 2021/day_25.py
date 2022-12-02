from utilities import load_data


YEAR = 2021
DAY = 25
input_data = load_data(year=YEAR, day=DAY)
# input_data = '''v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>'''
input_data = input_data.splitlines()

h = len(input_data)
w = len(input_data[0])
cukes = {}
for y in range(h):
    for x in range(w):
        cukes[(x, y)] = input_data[y][x]

step = 0
while True:
    east_moves = set()
    south_moves = set()
    for loc, cuke in cukes.items():
        if cuke == '.':
            continue
        x, y = loc
        if cuke == '>':
            x += 1
            x %= w
            if cukes[(x, y)] == '.':
                east_moves.add(loc)
    if east_moves:
        for loc in east_moves:
            ch = cukes[loc]
            cukes[loc] = '.'
            x, y = loc
            if ch == '>':
                x += 1
                x %= w
                if cukes[(x, y)] in '>v':
                    continue
            cukes[(x, y)] = ch
    for loc, cuke in cukes.items():
        if cuke == '.':
            continue
        x, y = loc
        if cuke == 'v':
            y += 1
            y %= h
            if cukes[(x, y)] == '.':
                south_moves.add(loc)
    if south_moves:
        for loc in south_moves:
            ch = cukes[loc]
            cukes[loc] = '.'
            x, y = loc
            if ch == 'v':
                y += 1
                y %= h
                if cukes[(x, y)] in '>v':
                    continue
            cukes[(x, y)] = ch
    if east_moves or south_moves:
        step += 1
        for y in range(h):
            s = ''
            for x in range(w):
                ch = cukes[(x, y)]
                s += ch if ch in '>v' else ' '
            print(s)
        print()
        print()
    else:
        step += 1
        break


answer = step
print(answer)
