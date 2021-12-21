from utilities import load_data


YEAR = 2015
DAY = 8
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


def word_score(word):
    score = 0
    i = 0
    while i < len(word):
        s = word[i: i+4]
        if s.startswith('\\\\') or s.startswith('\\"'):
            score += 1
            i += 2
        elif s.startswith('\\x'):
            try:
                int(s.replace('\\', '0'), 16)
                score += 3
                i += 4
            except ValueError:
                i += 1
        elif s.startswith('"'):
            score += 1
            i += 1
        else:
            i += 1
    return score


def upscore(word):
    score = 0
    for ch in word:
        score += 1
        score += ch in '"\\'
    return score + 2


answer = 0
for n, word in enumerate(input_data):
    print(f'Working on word {n+1}')
    answer += word_score(word)

print(answer)

answer = 0
for word in input_data:
    answer += upscore(word) - len(word)

print(answer)