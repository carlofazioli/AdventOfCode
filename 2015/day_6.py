from utilities import load_data


YEAR = 2015
DAY = 6
input_data = load_data(year=YEAR, day=DAY)


lights = [[0]*1000 for _ in range(1000)]

for i in input_data.splitlines():
    a, b = i.split(' through ')
    a = a.split(' ')
    instruction = ''.join(a[:-1])
    x0, y0 = list(map(int, a[-1].split(',')))
    x1, y1 = list(map(int, b.split(',')))
    for y in range(y0, y1+1):
        for x in range(x0, x1+1):
            if 'off' in instruction:
                lights[y][x] = max(lights[y][x]-1, 0)
            if 'on' in instruction:
                lights[y][x] += 1
            if 'toggle' in instruction:
                lights[y][x] += 2

answer = sum(sum(r) for r in lights)
print(answer)
