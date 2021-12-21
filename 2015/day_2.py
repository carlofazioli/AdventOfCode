from utilities import load_data


YEAR = 2015
DAY = 2
input_data = load_data(year=YEAR, day=DAY)


input_data = input_data.splitlines()

area = 0
ribbon = 0
for box in input_data:
    x, y, z = list(map(int, box.split('x')))
    area += 2*(x*y + x*z + y*z) + min(x*y, y*z, x*z)
    ribbon += 2*(x+y+z-max(x, y, z)) + x*y*z

print(area)
print(ribbon)
