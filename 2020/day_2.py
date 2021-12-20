import utilities


pwds = utilities.input_to_list('day_2.txt')


def parse_pwd_row(row):
    r, l, p = row.replace(':', '').split(' ')
    lower, upper = map(int, r.split('-'))
    count = 0
    for ch in p:
        if ch == l:
            count += 1
    return lower <= count <= upper


def solve_part_1():
    return sum(parse_pwd_row(row) for row in pwds)


def parse_pwd_row_2(row):
    r, l, p = row.replace(':', '').split(' ')
    lower, upper = map(int, r.split('-'))
    return (p[lower-1] == l) ^ (p[upper-1] == l)


def solve_part_2():
    return sum(parse_pwd_row_2(row) for row in pwds)
