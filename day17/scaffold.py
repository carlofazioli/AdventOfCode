from intcode import IntCodeComputer


pc = IntCodeComputer(source='input', buffered=True)
result = pc.run()
camera_out = result[0]


def render(screen):
    while screen:
        row = []
        while screen:
            ch = screen.pop(0)
            if ch == 10:
                break
            row.append(chr(ch))
        print(''.join(row))


render(camera_out)