from utilities import load_data


YEAR = 2016
DAY = 3
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


count = 0
for triangle in input_data:
    a, b, c = list(map(int, triangle.split()))
    valid = True
    valid &= a+b > c
    valid &= a+c > b
    valid &= b+c > a
    count += valid

print(count)


count = 0
triple_rows = [input_data[i:i+3] for i in range(0, len(input_data), 3)]
for triple in triple_rows:
    a = list(map(int, triple[0].split()))
    b = list(map(int, triple[1].split()))
    c = list(map(int, triple[2].split()))
    for col in range(3):
        valid = True
        valid &= a[col]+b[col] > c[col]
        valid &= a[col]+c[col] > b[col]
        valid &= b[col]+c[col] > a[col]
        count += valid

print(count)
