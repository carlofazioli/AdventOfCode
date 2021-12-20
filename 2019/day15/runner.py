from intcode import IntCodeComputer
import random


class Map:
    def __init__(self):
        self.droid_location = (0, 0)
        self.map = {self.droid_location: 'S'}
        self.move_codes = {
            # Y increases downward (typical of AoC problems and others):
            1: (0, -1),
            2: (0, 1),
            3: (-1, 0),
            4: (1, 0),
        }

    def unset(self):
        self.map[self.droid_location] = 'x'

    def update(self, move, result):
        x, y = self.droid_location
        vx, vy = self.move_codes[move]
        if result == 0:
            # The droid hit a wall:
            dest = self.map.get((x + vx, y + vy))
            if dest:
                assert dest == '#'
            self.map[(x + vx, y + vy)] = '#'
            return 0
        if result == 1:
            # Mark solution path with plus signs:
            self.map[self.droid_location] = '+'
            self.droid_location = (x + vx, y + vy)
            return 0
        if result == 2:
            self.map[self.droid_location] = '+'
            self.droid_location = (x + vx, y + vy)
            self.map[self.droid_location] = 'O'
            return self.droid_location

    def draw(self):
        xbounds, ybounds = self.get_bounds()
        print(''.join(['#']*(xbounds[1] + 1 - xbounds[0])))
        for y in range(ybounds[1]+1, ybounds[0], -1):
            row = []
            for x in range(xbounds[0], xbounds[1]+1):
                # if (x, y) == self.droid_location:
                #     if self.map.get((x, y), ' ') != 'G':
                #         row.append('D')
                # else:
                row.append(self.map.get((x, y), ' '))
            print(''.join(row))
        print(''.join(['#']*(xbounds[1] + 1 - xbounds[0])))

    def get_bounds(self):
        xmin = 0
        xmax = 0
        ymin = 0
        ymax = 0
        for loc in self.map.keys():
            x = loc[0]
            y = loc[1]
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y
        return [xmin, xmax], [ymin, ymax]


class AI:
    # LOL "AI"
    def __init__(self):
        self.map = Map()

    def move(self, result=None):
        return random.randint(1, 4)


if __name__ == '__main__':

    pc = IntCodeComputer(source='input', buffered=True)
    i_robot = AI()

    result = None

    # LOL total garbage:
    for _ in range(1000000):

        move = i_robot.move(result)
        ic_out = pc.run(move)
        result = ic_out[0][0]
        update = i_robot.map.update(move, result)
        if update != 0:
            print(update)
            # break
        # print()
        # print('move: ' + str(move) + '\tresult: ' + str(result))
        # m.draw()
        # print()

    i_robot.map.draw()




