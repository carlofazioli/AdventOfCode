from intcode import IntCodeComputer


shapes = {
    0: ' ',
    1: 'X',
    2: '=',
    3: '-',
    4: 'o',
}


def get_blocks(ic_output):
    blocks = {}
    while ic_output:
        x = ic_output.pop(0)
        y = ic_output.pop(0)
        tile_id = ic_output.pop(0)
        if x == -1:
            blocks[(x, y)] = tile_id
        else:
            blocks[(x, y)] = shapes[tile_id]
    return blocks


def draw_frame(blocks):
    xmax = 43
    ymax = 21
    paddle = 0
    ball = 0
    for j in range(ymax + 1):
        row = []
        for i in range(xmax+1):
            symbol = blocks[(i, j)]
            row.append(symbol)
            if symbol == '-':
                paddle = i
            if symbol == 'o':
                ball = i
        print(''.join(row))
    print('SCORE: ', blocks.get((-1, 0), 0))
    return paddle, ball


def joystick():
    joystick_raw = input()
    if joystick_raw == '':
        return 0
    else:
        return int(joystick_raw)


class AI:
    def __init__(self):
        self.last_ball_x = 0

    def act(self, paddle, ball):
        if paddle < ball:
            action = 1
        elif paddle == ball:
            action = 0
        elif paddle > ball:
            action = -1
        return action




if __name__ == '__main__':

    screen = {}
    pc = IntCodeComputer(source='input2', buffered=True)
    last_starfighter = AI()

    # Start game:
    result = pc.run(0)
    screen.update(get_blocks(result))

    while True:
        paddle, ball = draw_frame(screen)
        # inp = joystick()
        act = last_starfighter.act(paddle, ball)
        print(act)
        inp = act
        result = pc.run(int(inp))
        screen.update(get_blocks(result))

