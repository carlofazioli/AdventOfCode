from utilities import load_data
import json


YEAR = 2015
DAY = 12
input_data = load_data(year=YEAR, day=DAY)


d = json.loads(input_data)


def count(j):
    if isinstance(j, list):
        return sum(count(item) for item in j)
    if isinstance(j, dict):
        if 'red' not in j.values():
            return sum(count(item) for item in j.values())
        else:
            return 0
    if isinstance(j, int):
        return j
    return 0


answer = count(d)
print(answer)