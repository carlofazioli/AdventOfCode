from utilities import load_data

YEAR = 2021
DAY = 3
input_data = load_data(year=YEAR, day=DAY)

# Split input into a list of str:
input_data = input_data.splitlines()

part = 1

gamma = ''
epsilon = ''
for i in range(len(input_data[0])):
    count_0 = 0
    count_1 = 0
    for b in input_data:
        if b[i] == '0':
            count_0 += 1
        if b[i] == '1':
            count_1 += 1
    if count_0 > count_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

answer = int(gamma, 2) * int(epsilon, 2)
print(gamma)
print(epsilon)

n = len(input_data[0])
N = len(input_data)
count_ones = [0]*n
for b in input_data:
    count_ones = [a+(b == '1') for a, b in zip(count_ones, b)]
gamma = ''.join([str(1*(d > N/2)) for d in count_ones])
epsilon = ''.join([str(1*(d < N/2)) for d in count_ones])

print(gamma)
print(epsilon)

# submit(answer, part)

input_data = load_data()

# Split input into a list of str:
input_data = input_data.splitlines()

oxy_list = []
co2_list = []

for b in input_data:
    if b[0] == '0':
        oxy_list.append(b)
    else:
        co2_list.append(b)
# At this point, the thing called oxy_list contains all the
# values that start with '0'.  But, if co2_list is longer,
# then that's really the list we should be using to find the
# ox value.
if len(co2_list) >= len(oxy_list):
    oxy_list, co2_list = co2_list, oxy_list

oxy = ''
co2 = ''
for p in range(n):
    candidates = 0
    count = 0
    for b in input_data:
        if b.startswith(oxy):
            candidates += 1
            count += b[p] == '1'
    if count >= candidates - count:
        oxy += '1'
    else:
        oxy += '0'
    candidates = 0
    count = 0
    for b in input_data:
        if b.startswith(oxy):
            candidates += 1
            count += b[p] == '1'
    if count >= candidates - count:
        co2 += '0'
    else:
        co2 += '1'

ox = ''
for i in range(12):
    count_0 = 0
    count_1 = 0
    for b in input_data:
        if b[i] == '0':
            count_0 += 1
        if b[i] == '1':
            count_1 += 1
    if count_1 >= count_0:
        keep_digit = '1'
    else:
        keep_digit = '0'
    keep_list = []
    for b in input_data:
        if b[i] == keep_digit:
            keep_list.append(b)
    input_data = keep_list
    if len(input_data) == 1:
        ox = input_data[0]


input_data = load_data()

# Split input into a list of str:
input_data = input_data.splitlines()

co2 = ''
for i in range(12):
    count_0 = 0
    count_1 = 0
    for b in input_data:
        if b[i] == '0':
            count_0 += 1
        if b[i] == '1':
            count_1 += 1
    if count_1 >= count_0:
        keep_digit = '0'
    else:
        keep_digit = '1'
    keep_list = []
    for b in input_data:
        if b[i] == keep_digit:
            keep_list.append(b)
    input_data = keep_list
    if len(input_data) == 1:
        co2 = input_data[0]

answer = int(ox, 2) * int(co2, 2)
print(answer)
# submit(answer, 2)
