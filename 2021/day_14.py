from copy import copy
from datetime import datetime
import itertools
import collections

from utilities import load_data, submit

input_data = load_data(day=14)

# input_data = '''NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C'''

# Split input into a list of str:
# input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))

tmp, rules_list = input_data.split('\n\n')

rules = {}
rules_list = rules_list.splitlines()
for r in rules_list:
    a, b = r.split(' -> ')
    rules[a] = b

# for i in range(10):
#     t0 = datetime.now()
#     pairs = [tmp[i:i+2] for i in range(len(tmp)-1)]
#     tmp = ''
#     for p in pairs:
#         tmp += p[0] + rules.get(p, '')
#     tmp += p[1]
#     dt = datetime.now() - t0
#     print(dt.total_seconds())
#
# letters = collections.Counter(tmp)
# quantities = list(letters.values())
# quantities.sort()
# answer = quantities[-1] - quantities[0]
# print(answer)

start_letter = tmp[0]
end_letter = tmp[-1]

pair_counts = collections.defaultdict(int)
init_pairs = [tmp[i:i+2] for i in range(len(tmp)-1)]
for pair in init_pairs:
    pair_counts[pair] += 1

for _ in range(40):
    new = collections.defaultdict(int)
    for pair, count in pair_counts.items():
        if count:
            new[pair[0] + rules[pair]] += count
            new[rules[pair] + pair[1]] += count
    pair_counts = new

letter_counts = collections.defaultdict(int)
for pair, count in pair_counts.items():
    letter_counts[pair[0]] += count
    letter_counts[pair[1]] += count

letter_counts[start_letter] += 1
letter_counts[end_letter] += 1
quantities = [q//2 for q in letter_counts.values()]
quantities.sort()
answer = quantities[-1] - quantities[0]
print(answer)