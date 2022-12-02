from utilities import load_data


YEAR = 2016
DAY = 2
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()

x = 0
y = 0
sequence = []
for line in input_data:
    for ch in line:
        if ch == 'L':
            x -= 1
            x = max(x, -1)
        if ch == 'R':
            x += 1
            x = min(x, 1)
        if ch == 'U':
            y += 1
            y = min(y, 1)
        if ch == 'D':
            y -= 1
            y = max(y, -1)
    sequence.append([x, y])

print(sequence)


x = -2
y = 0
sequence = []
for line in input_data:
    for ch in line:
        if ch == 'L':
            x -= 1
            if abs(x) + abs(y) > 2:
                x += 1
        if ch == 'R':
            x += 1
            if abs(x) + abs(y) > 2:
                x -= 1
        if ch == 'U':
            y += 1
            if abs(x) + abs(y) > 2:
                y -= 1
        if ch == 'D':
            y -= 1
            if abs(x) + abs(y) > 2:
                y += 1
    sequence.append([x, y])

print(sequence)