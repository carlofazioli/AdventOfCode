from utilities import load_data


YEAR = 2015
DAY = 16
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


mfcsam = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
'''

compounds = {}
for row in mfcsam.splitlines():
    n, q = row.split(': ')
    compounds[n] = int(q)


keep = []
for sue in input_data:
    entry = []
    sue = sue.split(', ')
    idx, prop, val = sue[0].split(': ')
    idx = int(idx.split(' ')[1])
    entry.append(idx)
    entry.append([prop, int(val)])
    for pair in sue[1:]:
        pair = pair.split(': ')
        entry.append([pair[0], int(pair[1])])
    keep.append(entry)


new = []
while len(keep) > 1:
    for sue in keep:
        valid = True
        for pair in sue[1:]:
            if pair[0] in ['cats', 'trees']:
                valid &= pair[1] > compounds[pair[0]]
            elif pair[0] in ['pomeranians', 'goldfish']:
                valid &= pair[1] < compounds[pair[0]]
            else:
                valid &= pair[1] == compounds[pair[0]]
        if valid:
            new.append(sue)
    keep = new

answer = keep[0][0]
print(answer)
