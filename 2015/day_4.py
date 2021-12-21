import hashlib

from utilities import load_data


YEAR = 2015
DAY = 4
input_data = load_data(year=YEAR, day=DAY)

i = 0
found = False
while not found:
    result = hashlib.md5((input_data+str(i)).encode()).hexdigest()
    found = result.startswith('000000')
    if i == 1000000000:
        break
    i += 1

answer = i-1
print(answer)
