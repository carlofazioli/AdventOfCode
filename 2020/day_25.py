def transform(val, subject):
    val *= subject
    val %= 20201227
    return val


key_1 = 17115212
key_2 = 3667832

loop_1 = 8217635
loop_2 = 20035918

# val = 1
# for i in range(20201227):
#     val = transform(val, 7)
#     if val == key_1:
#         loop_1 = i+1


def make_pubkey(loop_size):
    val = 1
    for i in range(loop_size):
        val = transform(val, 7)
    return val


def make_encryp(pubkey, loop_size):
    val = 1
    for i in range(loop_size):
        val = transform(val, pubkey)
    return val


e_1 = make_encryp(key_2, loop_1)
e_2 = make_encryp(key_1, loop_2)