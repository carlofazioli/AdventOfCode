def get_digits(n):
    d = list(str(n))
    return list(map(int, d))

def part1(n):
    digits = get_digits(n)
    has_adjacent = False
    monotonic = True
    for i, j in zip(digits[:-1], digits[1:]):
        if i == j:
            has_adjacent = True
        if i > j:
            monotonic = False
    return has_adjacent and monotonic

def part2(n):
    digits = get_digits(n)
    groups = [0]
    for loc, (i, j) in enumerate(zip(digits[:-1], digits[1:])):
        if i < j:
            groups.append(loc+1)
    groups.append(6)
    diffs = [j-i for i,j in zip(groups[:-1], groups[1:])]
    if 2 in diffs:
        return True
    else:
        return max(diffs) < 2


if __name__ == '__main__':
    
    ok1 = 0
    ok2 = 0

    for n in range(245318, 765748):
        if part1(n):
            ok1 += 1
            if part2(n):
                ok2 += 1

    print(ok1, ok2)
