from utilities import load_data

YEAR = 2021
DAY = 4
input_data = load_data(year=YEAR, day=DAY)


# Split input into a list of str:
# input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))


part = 1

input_data = input_data.split('\n\n')

vals = list(map(int, input_data[0].split(',')))

boards = []
for b in input_data[1:]:
    b = b.split('\n')
    for i, row in enumerate(b):
        row = row.strip().replace('  ', ' ')
        b[i] = list(map(int, row.split(' ')))
    boards.append(b)

def check_bingo_card(b):
    winning = False
    score = 0
    for row in b:
        if row == ['X', 'X', 'X', 'X', 'X']:
            winning = True
            break
    for col in range(5):
        if [row[col] for row in b] == ['X', 'X', 'X', 'X', 'X']:
            winning = True
            break
    if winning:
        for row in b:
            for item in row:
                if isinstance(item, int):
                    score += item
    return winning, score


def mark_bingo_card(n, b):
    for i, row in enumerate(b):
        for j, item in enumerate(row):
            if item == n:
                row[j] = 'X'
    return b


for v in vals:
    winning_indices = []
    for i, b in enumerate(boards):
        b = mark_bingo_card(v, b)
        w, s = check_bingo_card(b)
        if w:
            answer = v * s
            winning_indices.append(i)
    if winning_indices:
        winning_indices.sort(reverse=True)
        for idx in winning_indices:
            boards.pop(idx)

print(answer)