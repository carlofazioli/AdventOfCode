import pexpect
import argparse


class Hull:
    def __init__(self):
        self.direction = 0
        self.loc = (0, 0)
        self.hull = {
            (0, 0): 1,
        }
        self.movements = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0),
        }
        self.has_painted = 0

    def update(self, painter_response):
        # Paint the current location:
        old_color = self.hull[self.loc]
        self.hull[self.loc] = painter_response[0]
        new_color = self.hull[self.loc]
        if new_color != old_color:
            self.has_painted += 1

        # Rotate:
        self.direction += (-1 + 2*painter_response[1])
        self.direction %= 4

        # Move forward 1:
        new_x = self.loc[0] + self.movements[self.direction][0]
        new_y = self.loc[1] + self.movements[self.direction][1]
        self.loc = (new_x, new_y)
        if self.loc not in self.hull:
            self.hull[self.loc] = 0

        return self.hull[self.loc]

    def display_hull(self):
        xmax = 0
        xmin = 0
        ymax = 0
        ymin = 0
        for key in self.hull:
            x = key[0]
            y = key[1]
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y
        reg = []
        for j in range(ymax, ymin-1, -1):
            row = ''
            for i in range(xmin, xmax+1):
                if self.hull.get((i, j), 0):
                    row += 'X'
                else:
                    row += ' '
            reg.append(row)

        print('x: ', xmin, xmax)
        print('y: ', ymin, ymax)
        print('reg:' )
        for r in reg:
            print(r)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', dest='source', default='input')
    args = parser.parse_args()

    h = Hull()
    pc = pexpect.spawn('python', ['runner.py'])

    inp = 1
    pc.sendline(str(inp))

    # This is just the input echoed back:
    pc.expect([b'\r\n', pexpect.EOF])

    # The color:
    pc.expect([b'\r\n', pexpect.EOF])
    out = pc.before
    color = int(out.split(b'\r\n')[0])

    # The turn:
    pc.expect([b'\r\n', pexpect.EOF])
    out = pc.before
    turn = int(out.split(b'\r\n')[0])

    response = [color, turn]

    while response:
        try:
            inp = h.update(response)
            pc.sendline(str(inp))

            # This is just the input echoed back:
            _ = pc.expect([b'\r\n', pexpect.EOF])

            # The color:
            _ = pc.expect([b'\r\n', pexpect.EOF])
            out = pc.before
            color = int(out.split(b'\r\n')[0])

            # The turn:
            pc.expect([b'\r\n', pexpect.EOF])
            out = pc.before
            turn = int(out.split(b'\r\n')[0])

            response = [color, turn]

            print(len(h.hull))

        except ValueError:
            h.display_hull()
            break

    input()






