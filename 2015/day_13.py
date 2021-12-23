from collections import defaultdict
import itertools
from utilities import load_data


YEAR = 2015
DAY = 13
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


attendees = set()
attendees.add('carlo')
for row in input_data:
    attendees.add(row.split(' ')[0])

happinesses = defaultdict(dict)
for row in input_data:
    attendee, result = row.split(' would ')
    result = result.split(' ')
    sign = result[0]
    amount = int(result[1])
    target = result[-1][:-1]
    if sign == 'lose':
        amount *= -1
    happinesses[attendee][target] = amount
    happinesses[attendee]['carlo'] = 0
    happinesses['carlo'][attendee] = 0

answer = 0
for p in itertools.permutations(attendees):
    cost = 0
    for i in range(len(p)):
        cost += happinesses[p[i]][p[(i+1) % len(p)]]
        cost += happinesses[p[(i+1) % len(p)]][p[i]]
    answer = max(answer, cost)

print(answer)