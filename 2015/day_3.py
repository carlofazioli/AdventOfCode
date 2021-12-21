from utilities import load_data


YEAR = 2015
DAY = 3
input_data = load_data(year=YEAR, day=DAY)


visited = set()
loc = (0, 0)
visited.add(loc)
for ch in input_data:
    x, y = loc
    if ch == '^':
        y += 1
    if ch == '<':
        x -= 1
    if ch == 'v':
        y -= 1
    if ch == '>':
        x += 1
    loc = (x, y)
    visited.add(loc)

answer = len(visited)
print(answer)


visited = set()
santa_loc = (0, 0)
robo_loc = (0, 0)
visited.add(santa_loc)
for i, ch in enumerate(input_data):
    if i % 2 == 0:
        x, y = santa_loc
        if ch == '^':
            y += 1
        if ch == '<':
            x -= 1
        if ch == 'v':
            y -= 1
        if ch == '>':
            x += 1
        santa_loc = (x, y)
        visited.add(santa_loc)
    else:
        x, y = robo_loc
        if ch == '^':
            y += 1
        if ch == '<':
            x -= 1
        if ch == 'v':
            y -= 1
        if ch == '>':
            x += 1
        robo_loc = (x, y)
        visited.add(robo_loc)

answer = len(visited)
print(answer)