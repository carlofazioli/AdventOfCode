from utilities import load_data


YEAR = 2021
DAY = 13
input_data = load_data(year=YEAR, day=DAY)

points, folds = input_data.split('\n\n')
points = points.splitlines()
folds = folds.splitlines()

locs = set(tuple(map(int, p.split(','))) for p in points)

for f in folds:
    fold_loc = f.split(' ')[-1]
    d, val = fold_loc.split('=')
    val = int(val)
    new = set()
    if d == 'x':
        for x, y in locs:
            if x < val:
                new.add((x, y))
            else:
                x = 2*val - x
                new.add((x, y))
    if d == 'y':
        for x, y in locs:
            if y < val:
                new.add((x, y))
            else:
                y = 2*val - y
                new.add((x, y))
    locs = new

X = max(x for x, y in locs)
Y = max(y for x, y in locs)
for y in range(Y+1):
    for x in range(X + 1):
        if (x, y) in locs:
            print('#', end='')
        else:
            print(' ', end='')
    print()
