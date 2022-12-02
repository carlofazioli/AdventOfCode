from utilities import load_data


YEAR = 2016
DAY = 6
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()

counts = [{}, {}, {}, {}, {}, {}, {}, {}]
for word in input_data:
    for i in range(8):
        ch = word[i]
        if ch not in counts[i]:
            counts[i][ch] = 0
        counts[i][ch] += 1

message = ''
for i in range(8):
    data = [[ch, count] for ch, count in counts[i].items()]
    data.sort(key=lambda x: x[1], reverse=True)
    message += data[0][0]

print(message)

message = ''
for i in range(8):
    data = [[ch, count] for ch, count in counts[i].items()]
    data.sort(key=lambda x: x[1])
    message += data[0][0]

print(message)