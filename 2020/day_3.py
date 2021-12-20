import utilities


map_rows = utilities.input_to_list('day_3.txt')


def count_trees(m, dx, dy):
    width = len(m[0])
    count = 0
    col = 0
    for row in m[::dy]:
        count += row[col] == '#'
        col += dx
        col %= width
    return count


def solve_part_1():
    return count_trees(map_rows, 3, 1)


def solve_part_2():
    v = count_trees(map_rows, 1, 1)
    w = count_trees(map_rows, 3, 1)
    x = count_trees(map_rows, 5, 1)
    y = count_trees(map_rows, 7, 1)
    z = count_trees(map_rows, 1, 2)
    return v*w*x*y*z