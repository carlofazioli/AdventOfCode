import utilities


passes = utilities.input_to_list('day_5.txt')


def get_seat_id(p):
    row = int(p[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(p[7:].replace('R', '1').replace('L', '0'), 2)
    return row*8 + col


def solve_part_1():
    return max(get_seat_id(p) for p in passes)


def solve_part_2():
    all_ids = [get_seat_id(p) for p in passes]
    for i in range(max(all_ids)):
        if i-1 in all_ids and i not in all_ids and i+1 in all_ids:
            print(i)


print(solve_part_1())
print(solve_part_2())
