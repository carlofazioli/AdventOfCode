from utilities import load_data


YEAR = 2021
DAY = 10
input_data = load_data(year=YEAR, day=DAY)

# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))

# scores = {
#     ')': 3,
#     ']': 57,
#     '}': 1197,
#     '>': 25137
# }
scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
matches = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
answer = 0
incomplete = []
for line in input_data:
    corrupted = False
    stack = ''
    for ch in line:
        if corrupted:
            break
        if ch in ['(', '[', '{', '<']:
            stack += ch
        else:
            if stack[-1] == matches[ch]:
                stack = stack[:-1]
            else:
                answer += scores[ch]
                corrupted = True
    if not corrupted:
        incomplete.append(line)

autocompletes = []
for line in incomplete:
    stack = ''
    for ch in line:
        if ch in ['(', '[', '{', '<']:
            stack += ch
        else:
            if stack[-1] == matches[ch]:
                stack = stack[:-1]
            else:
                assert False
    line_score = 0
    for ch in stack[::-1]:
        line_score *= 5
        line_score += scores[matches[ch]]
    autocompletes.append(line_score)

autocompletes.sort()
answer = autocompletes[len(autocompletes)//2]

print(answer)