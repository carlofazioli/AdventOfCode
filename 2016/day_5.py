import hashlib
from utilities import load_data


YEAR = 2016
DAY = 5


door_id = 'ojvtpuvg'

# pw = ''
# idx = 0
# for _ in range(8):
#     found = False
#     while not found:
#         s = door_id + str(idx)
#         result = hashlib.md5(s.encode()).hexdigest()
#         found = result.startswith('00000')
#         idx += 1
#     pw += result[5]
#     print(pw)
#
# print(pw)


pw = ['X']*8
idx = 0
valid_hashes = 0
while 'X' in pw:
    found = False
    while not found:
        s = door_id + str(idx)
        result = hashlib.md5(s.encode()).hexdigest()
        found = result.startswith('00000')
        idx += 1
    try:
        position = int(result[5])
        if position >= 8 or pw[position] != 'X':
            continue
        ch = result[6]
        pw[position] = ch
        print(''.join(pw))
        valid_hashes += 1
    except ValueError:
        pass

print(''.join(pw))
