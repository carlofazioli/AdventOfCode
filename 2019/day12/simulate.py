import parse
import numpy as np


form = '<x={}, y={}, z={}>'


def parse_source(source):
    moon_pos = []
    with open(source) as f:
        for line in f:
            res = parse.parse(form, line)
            moon_pos.append(list(map(int, list(res))))
    return moon_pos


class Moon:
    def __init__(self,
                 pos):
        self.pos = pos
        self.vel = [0, 0, 0]

    def update_vel(self, other):
        for i in range(3):
            if self.pos[i] < other.pos[i]:
                self.vel[i] += 1
            elif self.pos[i] > other.pos[i]:
                self.vel[i] -= 1

    def move(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def disp(self):
        print('pos=' + form.format(self.pos[0], self.pos[1], self.pos[2]),
              'vel=' + form.format(self.vel[0], self.vel[1], self.vel[2]))

    def potential(self):
        return sum(map(abs, self.pos))

    def kinetic(self):
        return sum(map(abs, self.vel))


def evolve_moons(moons, max_steps, break_on_cycle=False):

    n = len(moons)
    init_conf = []
    for m in range(n):
        init_conf += moons[m].pos + moons[m].vel

    sys_energy = 0
    for k in range(max_steps):

        for i in range(n):
            for j in range(i, n):
                mi = moon_list[i]
                mj = moon_list[j]
                mi.update_vel(mj)
                mj.update_vel(mi)

        for i in range(n):
            moon_list[i].move()

        sys_energy = 0
        for i in range(n):
            pot = moon_list[i].potential()
            kin = moon_list[i].kinetic()
            sys_energy += pot*kin

        conf = []
        for i in range(n):
            conf += moon_list[i].pos + moon_list[i].vel

        if conf == init_conf and break_on_cycle:
            return k+1

    return sys_energy


if __name__ == '__main__':

    posits = parse_source('input')
    moon_list = [Moon(p) for p in posits]
    sys_e = evolve_moons(moon_list, 1000, break_on_cycle=False)
    print(sys_e)

    cycles = []
    for exp in range(1, 4):
        posits = parse_source('input_split_' + str(exp))
        moon_list = [Moon(p) for p in posits]
        cyc = evolve_moons(moon_list, 1000000, break_on_cycle=True)
        cycles.append(cyc)

    t1 = np.lcm(cycles[0], cycles[1])
    ans = np.lcm(t1, cycles[2])
    print(ans)

    input()



