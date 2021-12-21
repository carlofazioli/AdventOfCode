from string import ascii_lowercase


with open('input_data/day_6.txt') as f:
    groups_raw = f.read()

groups = groups_raw.split('\n\n')


def count_questions(g):
    g = g.split('\n')
    count = 0
    for ch in ascii_lowercase:
        f = lambda x: ch in x
        count += any(map(f, g))
    return count


def solve_part_1():
    return sum(count_questions(g) for g in groups)


def count_questions_2(g):
    g = g.split('\n')
    count = 0
    for ch in ascii_lowercase:
        f = lambda x: ch in x
        count += all(map(f, g))
    return count


def solve_part_2():
    return sum(count_questions_2(g) for g in groups)


print(solve_part_1())
print(solve_part_2())
input()
