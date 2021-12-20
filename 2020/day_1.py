import utilities


def solve_part_1():

    vals = list(map(int, utilities.input_to_list('day_1.txt')))
    for v in vals:
        for w in vals:
            print(v,w,v+w)
            if v + w == 2020:
                return v*w
    return 'No match found'


def solve_part_2():
    vals = list(map(int, utilities.input_to_list('day_1.txt')))
    for u in vals:
        for v in vals:
            for w in vals:
                if u+v+w == 2020:
                    return u*v*w
    return 'No match found'