from utilities import load_data


YEAR = 2016
DAY = 1
input_data = load_data(year=YEAR, day=DAY)
# input_data = 'R8, R4, R4, R8'
input_data = input_data.split(', ')


x = 0
y = 0
dir = [0, 1]
for step in input_data:
    turn = step[0]
    d = int(step[1:])
    if turn == 'R':
        if dir == [1, 0]:
            dir = [0, -1]
        elif dir == [0, 1]:
            dir = [1, 0]
        elif dir == [-1, 0]:
            dir = [0, 1]
        elif dir == [0, -1]:
            dir = [-1, 0]
    elif turn == 'L':
        if dir == [1, 0]:
            dir = [0, 1]
        elif dir == [0, 1]:
            dir = [-1, 0]
        elif dir == [-1, 0]:
            dir = [0, -1]
        elif dir == [0, -1]:
            dir = [1, 0]
    x += d*dir[0]
    y += d*dir[1]

answer = abs(x) + abs(y)
print(answer)


x = 0
y = 0
dir = [0, 1]
loc = (x, y)
locs = set()
locs.add(loc)
done = False
for step in input_data:
    if done:
        break
    turn = step[0]
    d = int(step[1:])
    if turn == 'R':
        if dir == [1, 0]:
            dir = [0, -1]
        elif dir == [0, 1]:
            dir = [1, 0]
        elif dir == [-1, 0]:
            dir = [0, 1]
        elif dir == [0, -1]:
            dir = [-1, 0]
    elif turn == 'L':
        if dir == [1, 0]:
            dir = [0, 1]
        elif dir == [0, 1]:
            dir = [-1, 0]
        elif dir == [-1, 0]:
            dir = [0, -1]
        elif dir == [0, -1]:
            dir = [1, 0]
    for _ in range(d):
        x += dir[0]
        y += dir[1]
        loc = (x, y)
        if loc in locs:
            answer = abs(x) + abs(y)
            done = True
            break
        else:
            locs.add(loc)

print(answer)