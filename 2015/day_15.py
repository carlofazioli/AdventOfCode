from utilities import load_data


YEAR = 2015
DAY = 15
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()

ingredients = []
for row in input_data:
    name, row = row.split(': ')
    properties = row.split(', ')
    ingredients.append([int(p.split(' ')[1]) for p in properties])


def score(quantities):
    score = 1
    for i in range(4):
        s = sum(q*r[i] for q, r in zip(quantities, ingredients))
        score *= s if s > 0 else 0
    cals = sum(q*r[4] for q, r in zip(quantities, ingredients))
    return score, cals


answer = 0
for q1 in range(1, 100):
    for q2 in range(1, 100):
        for q3 in range(1, 100):
            for q4 in range(1, 100):
                if sum([q1, q2, q3, q4]) != 100:
                    continue
                s, c = score([q1, q2, q3, q4])
                if c == 500:
                    answer = max(answer, s)

print(answer)