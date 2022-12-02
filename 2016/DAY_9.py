from utilities import load_data


YEAR = 2016
DAY = 9
input_data = load_data(year=YEAR, day=DAY)


def decompress(s):
    if '(' not in s:
        return s
    idx_left = s.index('(')
    idx_right = s.index(')')
    prefix = s[:idx_left]
    marker = s[idx_left+1:idx_right]
    suffix = s[idx_right+1:]
    data_len, reps = marker.split('x')
    data_len = int(data_len)
    reps = int(reps)
    data, suffix = suffix[:data_len], suffix[data_len:]
    return prefix + data*reps + decompress(suffix)


# input_data = decompress(input_data)
#
# answer = len(input_data)
# print(answer)


def decomp_len(s):
    if '(' not in s:
        return len(s)
    idx_left = s.index('(')
    idx_right = s.index(')')
    prefix = s[:idx_left]
    marker = s[idx_left+1:idx_right]
    suffix = s[idx_right+1:]
    data_len, reps = marker.split('x')
    data_len = int(data_len)
    reps = int(reps)
    data, suffix = suffix[:data_len], suffix[data_len:]
    return len(prefix) + decomp_len(data)*reps + decomp_len(suffix)


answer = decomp_len(input_data)

print(answer)