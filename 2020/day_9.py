import utilities


data = utilities.input_to_list('day_9.txt')
data = list(map(int, data))


def is_valid(n, preamble):
    for i in preamble:
        for j in preamble:
            if i + j == n:
                return True
    return False


def find_invalid(d):
    for i in range(25, len(d)):
        if not is_valid(d[i], d[i-25:i]):
            return d[i]


def find_range(d, t):
    for i in range(len(d)):
        for j in range(len(d)-i):
            s = sum(d[i:j])
            if s == t:
                return min(d[i:j]) + max(d[i:j])


t = find_invalid(data)
print(find_range(data, t))
