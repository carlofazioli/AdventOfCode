s = '1113122113'


def iterate(s):
    out = ''
    count = 0
    for ch in s:
        if count == 0:
            chunk = ch
            count = 1
        else:
            if ch == chunk:
                count += 1
            else:
                chunk = str(count) + chunk
                out += chunk
                chunk = ch
                count = 1
    chunk = str(count) + chunk
    out += chunk
    return out


for _ in range(50):
    s = iterate(s)
    print(len(s))