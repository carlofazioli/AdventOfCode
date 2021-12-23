from utilities import load_data


YEAR = 2015
DAY = 14
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


reindeerts = dict()
for row in input_data:
    deert, row = row.split(' can fly ')
    speed, row = row.split(' km/s for ')
    duration, row = row.split(' seconds, but then must rest for ')
    rest, row = row.split(' ')
    speed = int(speed)
    duration = int(duration)
    rest = int(rest)
    reindeerts[deert] = (speed, duration, rest)


def sim(speed, duration, rest, t):
    d = 0
    while t:
        if t >= duration:
            d += speed * duration
            t -= duration
        else:
            d += speed * t
            t = 0
        t -= min(t, rest)
    return d


answer = 0
for data in reindeerts.values():
    d = sim(*data, 2503)
    answer = max(answer, d)

print(answer)


scores = {deert: 0 for deert in reindeerts.keys()}
for t in range(1, 2504):
    distances = {deert: sim(*data, t) for deert, data in reindeerts.items()}
    m = max(d for d in distances.values())
