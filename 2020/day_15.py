starting = [0, 14, 6, 20, 1, 4]


class Game:
    def __init__(self, starting):
        self.starting = starting

    def play(self, n=2020):
        turn = 0
        spoken = []
        while turn < n:
            turn += 1
            if turn <= len(self.starting):
                spoken.append(self.starting[turn-1])
                continue
            recent = spoken[-1]
            if recent not in spoken[:-1]:
                spoken.append(0)
                continue
            else:
                age = spoken[::-1][1:].index(recent)+1
                spoken.append(age)
        return spoken


g = Game(starting)
out = g.play()
print(out[-1])


class GameV2(Game):
    def play(self, n=2020):
        times_spoken = dict()
        for turn, spoken in enumerate(self.starting):
            times_spoken[spoken] = [turn+1]
        turn += 2
        while turn <= n:
            times = times_spoken[spoken]
            if len(times) < 2:
                spoken = 0
            else:
                spoken = times[1] - times[0]
            if spoken not in times_spoken:
                times_spoken[spoken] = [turn]
            else:
                times_spoken[spoken].append(turn)
            if len(times_spoken[spoken]) > 2:
                times_spoken[spoken].pop(0)
            turn += 1
        return spoken


g2 = GameV2(starting)
out = g2.play(n=30000000)
print(out)