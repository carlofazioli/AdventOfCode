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

move_routine = 'A,B,A,C,A,A,C,B,C,B\n'
A = 'L,12,L,8,R,11,L,8,L,12\n'
B = 'L,99,L,9,L,99,R,9\n'
C = 'R,99,L,99,L,99\n'
video_feed = 'n\n'

part2_inp = []
part2_inp += list(map(ord, list(move_routine)))
part2_inp += list(map(ord, list(A)))
part2_inp += list(map(ord, list(B)))
part2_inp += list(map(ord, list(C)))
part2_inp += list(map(ord, list(video_feed)))

pc2 = IntCodeComputer(source='input.mod', buffered=True)
result = pc2.run(part2_inp)
print(result)
result = result[0]
print(''.join(list(map(chr, result))))

