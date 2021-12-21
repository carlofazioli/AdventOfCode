from utilities import load_data


YEAR = 2015
DAY = 1
input_data = load_data(year=YEAR, day=DAY)

floor = 0
pos = None
for i, ch in enumerate(input_data):
    floor += ch == '('
    floor -= ch == ')'
    if pos is None and floor == -1:
        pos = i + 1

print(floor)
print(pos)
