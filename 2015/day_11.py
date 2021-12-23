from string import ascii_lowercase
from utilities import load_data


YEAR = 2015
DAY = 11
input_data = load_data(year=YEAR, day=DAY)


def increment(pw):
    pw = list(pw)
    for i in range(7, -1, -1):
        n = chr(ord(pw[i]) + 1)
        if n in ascii_lowercase:
            pw[i] = n
            return ''.join(pw)
        else:
            pw[i] = 'a'
    return ''.join(pw)


def has_straight(pw):
    for i in range(len(ascii_lowercase)-2):
        straight = ascii_lowercase[i:i+3]
        if straight in pw:
            return True
    return False


def avoids_prohibited(pw):
    for prohibited in 'iol':
        if prohibited in pw:
            return False
    return True


def has_pairs(pw):
    count = 0
    for ch in ascii_lowercase:
        count += 2*ch in pw
        if count >= 2:
            return True
    return False


def is_valid(pw):
    return avoids_prohibited(pw) and has_pairs(pw) and has_straight(pw)


s = input_data
s = increment(s)
while not is_valid(s):
    s = increment(s)

print(s)

s = increment(s)
while not is_valid(s):
    s = increment(s)

print(s)
