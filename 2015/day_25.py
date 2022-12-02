from utilities import load_data


YEAR = 2015
DAY = 25
input_data = load_data(year=YEAR, day=DAY)

row = 2981
col = 3075


def index(r, c):
    return (c+r)*(c+r-1)//2 - r + 1


code = 20151125
mult = 252533
divi = 33554393

for _ in range(index(row, col)-1):
    code *= mult
    code %= divi

print(code)