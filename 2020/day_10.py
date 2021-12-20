import utilities


adapters = utilities.input_to_list('day_10.txt')
adapters = list(map(int, adapters))

adapters.sort()

adapters = [0] + adapters + [adapters[-1]+3]

diffs = [adapters[i+1]-adapters[i] for i in range(len(adapters)-1)]
diffs_copy = list(diffs)

ones = sum(map(lambda x: x==1, diffs))
tres = sum(map(lambda x: x==3, diffs))

print(ones*tres)

runs = []
while diffs:
    try:
        idx = diffs.index(3)
    except ValueError:
        idx = 0
    runs.append(idx)
    if idx == 0:
        idx += 1
    diffs = diffs[idx:]

ways = 1
fours = sum(map(lambda x:x==4, runs))
tres = sum(map(lambda x:x==3, runs))
twos = sum(map(lambda x:x==2, runs))

"""
By working it out by hand, a run of k diffs of 1 implies k-1 choices of adapters.
For 3 adapters, must choose at least 1 of them -> 7 choices.
For 2 adapters -> 4 choices
For 1 adapter -> 2 choices
"""

print((7**fours)*(4**tres)*(2**twos))