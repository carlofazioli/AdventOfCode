from collections import Counter
from utilities import load_data


YEAR = 2016
DAY = 4
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


def valid_room(r):
    encrypted_name, sector, checksum = r[:-10], r[-10:-7], r[-6:-1]
    counts = {}
    for ch in encrypted_name.replace('-', ''):
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    true_checksum = ''
    while len(true_checksum) < 5:
        new_letters = ''
        max_freq = max(counts.values())
        for ch, count in counts.items():
            if count == max_freq:
                new_letters += ch
        new_letters = list(new_letters)
        new_letters.sort()
        new_letters = ''.join(new_letters)
        for ch in new_letters:
            counts[ch] = 0
        true_checksum += new_letters
    true_checksum = true_checksum[:5]
    if true_checksum == checksum:
        return int(sector)
    else:
        return 0


answer = 0
for room in input_data:
    answer += valid_room(room)

print(answer)


def decrypt(r):
    encrypted_name, sector, checksum = r[:-10], r[-10:-7], r[-6:-1]
    sector = int(sector)
    sector %= 26
    decrypted_name = ''
    for ch in encrypted_name:
        if ch == '-':
            decrypted_name += ' '
            continue
        idx = ord(ch) - 97
        idx += sector
        idx %= 26
        decrypted_name += chr(idx+97)
    return decrypted_name, r[-10:-7]


for room in input_data:
    if valid_room(room):
        name, id = decrypt(room)
        if 'north' in name:
            print(name, id)