from string import ascii_lowercase
from utilities import load_data


YEAR = 2015
DAY = 5
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


def has_vowels(word):
    count = 0
    for ch in word:
        count += ch in 'aeiou'
    return count >= 3


def has_double(word):
    for ch in ascii_lowercase:
        if 2*ch in word:
            return True
    return False


answer = 0
for word in input_data:
    nice = has_vowels(word)
    nice &= has_double(word)
    for taboo in ['ab', 'cd', 'pq', 'xy']:
        nice &= taboo not in word
    answer += nice

print(answer)


def has_pair(word):
    for i in range(len(word)-3):
        pair = word[i:i+2]
        try:
            rest = word[i+2:]
            idx = rest.index(pair)
            print(f'{word} has repeated pair {pair} at indices {i} and {idx+i+2}:')
            print(f'{i*" "}{pair}{idx*" "}{pair}')
            return True
        except ValueError:
            pass
    print(f'{word} has no repeated pairs.')
    return False


def has_trio(word):
    for i in range(len(word)-2):
        trio = word[i:i+3]
        if trio[0] == trio[2]:
            print(f'{word} has nice trio {trio} at index {i}:')
            print(f'{i*" "}{trio}')
            return True
    print(f'{word} has no nice trios.')
    return False


answer = 0
for word in input_data:
    t = has_trio(word)
    p = has_pair(word)
    answer += t and p
    print(answer)
    print()

print(answer)
