from utilities import load_data


YEAR = 2021
DAY = 6
input_data = load_data(year=YEAR, day=DAY)


# Split input into a list of str:
input_data = input_data.splitlines()

# Convert to list of int:
# input_data = list(map(int, input_data))

fish_timers = list(map(int, input_data[0].split(',')))

fish_populations = {i: 0 for i in range(9)}
for t in fish_timers:
    fish_populations[t] += 1

for g in range(256):
    aged_fish = {i-1: fish_populations[i] for i in range(1, 9)}
    repro_fish = fish_populations[0]
    aged_fish[6] += repro_fish
    aged_fish[8] = repro_fish
    fish_populations = aged_fish


answer = sum(fish_populations.values())
print(answer)
# submit(answer, part)

