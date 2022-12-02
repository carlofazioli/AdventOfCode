from utilities import load_data


YEAR = 2016
DAY = 7
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


count = 0
for ip in input_data:
    seqs = []
    x = ip.split('[')
    for i in x:
        seqs += i.split(']')
    hypernet_seqs = seqs[1::2]
    net_seqs = seqs[::2]

    hypernet_abba = False
    for seq in hypernet_seqs:
        quads = [seq[i:i+4] for i in range(0, len(seq)-3)]
        for q in quads:
            hypernet_abba |= q[0] != q[1] and q[0] == q[3] and q[1] == q[2]
    if hypernet_abba:
        continue

    has_abba = False
    for seq in net_seqs:
        quads = [seq[i:i+4] for i in range(0, len(seq)-3)]
        for q in quads:
            has_abba |= q[0] != q[1] and q[0] == q[3] and q[1] == q[2]
    if has_abba:
        count += 1

print(count)

# PART 2

count = 0
for ip in input_data:
    seqs = []
    x = ip.split('[')
    for i in x:
        seqs += i.split(']')
    hypernet_seqs = seqs[1::2]
    net_seqs = seqs[::2]

    abas = []
    for seq in net_seqs:
        trios = [seq[i:i+3] for i in range(0, len(seq)-2)]
        for t in trios:
            if t[0] != t[1] and t[0] == t[2]:
                abas.append(t)
    if not abas:
        continue

    has_bab = False
    for seq in hypernet_seqs:
        trios = [seq[i:i + 3] for i in range(0, len(seq) - 2)]
        for t in trios:
            for aba in abas:
                if t[0] == aba[1] and t[1] == aba[0] and t[2] == aba[1]:
                    has_bab = True
    if has_bab:
        count += 1

print(count)