from utilities import load_data


YEAR = 2021
DAY = 20
input_data = load_data(year=YEAR, day=DAY)

algo, img = input_data.split('\n\n')
img = img.splitlines()

w = len(img[0])
h = len(img)

img_map = {}
for x in range(w):
    for y in range(h):
        img_map[(x, y)] = img[y][x]

for i in range(50):
    ch = '.' if i % 2 == 0 else '#'
    img_new = {}
    for x in range(-1-i, w+1+i):
        for y in range(-1-i, h+1+i):
            b = ''
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    b += img_map.get((x+dx, y+dy), ch)
            b = b.replace('#', '1')
            b = b.replace('.', '0')
            idx = int(b, 2)
            img_new[(x, y)] = algo[idx]
    img_map = img_new

answer = sum(1 for ch in img_map.values() if ch == '#')
print(answer)
