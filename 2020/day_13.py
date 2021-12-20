import utilities


bus = utilities.input_to_list('day_13.txt')

t = int(bus[0])
ids = bus[1].split(',')
running = []
indexes = []
for idx, i in enumerate(ids):
    try:
        running.append(int(i))
        indexes.append(idx)
    except ValueError:
        continue

residues = [i - t % i for i in running]

min_res = min(residues)
idx = residues.index(min_res)
bus_id = running[idx]

print(bus_id*min_res)

pairs = list(zip(running, indexes))

# pairs = [(17,0),(13,2),(19,3)]

pairs.sort(key=lambda x: -x[0])


# Sieve method: Chinese Remainder Theorem
x = 0
inc = 1
for p in pairs:
    a = p[1]
    n = p[0]
    while True:
        if x % n == (n-a)%n:
            inc *= n
            break
        x += inc

print(x)