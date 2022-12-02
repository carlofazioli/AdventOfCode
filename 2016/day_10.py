from collections import defaultdict
from utilities import load_data


YEAR = 2016
DAY = 10
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()

bots = defaultdict(list)
outputs = defaultdict(list)
while input_data:
    instruction = input_data.pop(0)
    instruction = instruction.split()
    if instruction[0] == 'value':
        chip = int(instruction[1])
        bot = int(instruction[-1])
        bots[bot].append(chip)
        continue
    bot = int(instruction[1])
    if len(bots[bot]) < 2:
        input_data.append(' '.join(instruction))
        continue
    bots[bot].sort()
    if bots[bot] == [17, 61]:
        answer = bot
    lo, hi = bots[bot]
    bots[bot] = []
    lo_type = instruction[5]
    lo_target = int(instruction[6])
    hi_type = instruction[-2]
    hi_target = int(instruction[-1])
    if lo_type == 'bot':
        bots[lo_target].append(lo)
    else:
        outputs[lo_target].append(lo)
    if hi_type == 'bot':
        bots[hi_target].append(hi)
    else:
        outputs[hi_target].append(hi)

print(answer)

answer = outputs[0][0] * outputs[1][0] * outputs[2][0]
print(answer)