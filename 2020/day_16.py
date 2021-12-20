with open('input_files/day_16.txt') as f:
    notes = f.read()


rules, my_ticket, nearby = notes.split('\n\n')


def parse_rules(rules):
    rules_list = rules.split('\n')
    rules_dict = dict(r.split(':') for r in rules_list)
    for k, v in rules_dict.items():
        rules_dict[k] = parse_ranges(v)
    return rules_dict


def parse_ranges(r):
    r = r.replace(' ', '')
    r = r.split('or')
    r = [list(map(int, i.split('-'))) for i in r]
    return r


def parse_ticket(t, range_dict):
    t = list(map(int, t.split(',')))
    error_rate = 0
    for val in t:
        valid = False
        for range_pair in range_dict.values():
            valid |= val_in_range(val, range_pair)
            if valid:
                continue
        if not valid:
            error_rate += val
    return error_rate


def val_in_range(val, range_pair):
    in_range = False
    for lower, upper in range_pair:
        in_range |= (lower <= val <= upper)
    return in_range


range_dict = parse_rules(rules)
tickets = nearby.split('\n')
valid_tix = []
total_error = 0
for ticket in tickets[1:]:
    err = parse_ticket(ticket, range_dict)
    total_error += err
    if err == 0:
        valid_tix.append(ticket)

print(total_error)

candidates = [list(range_dict.keys()) for _ in range(len(range_dict))]

valid_tix = [list(map(int, t.split(','))) for t in valid_tix]

finals = [0]*20


def whittle():
    for i in range(20):
        for t in valid_tix:
            val = t[i]
            removals = []
            for name in candidates[i]:
                if not val_in_range(val, range_dict[name]):
                    removals.append(name)
            for name in removals:
                idx = candidates[i].index(name)
                candidates[i].pop(idx)


def clean():
    idx = None
    name = None
    for i, row in enumerate(candidates):
        if len(row) == 1:
            idx = i
            name = row[0]
            finals[idx] = name
            break
    if name:
        for i, row in enumerate(candidates):
            if row:
                k = row.index(name)
                row.pop(k)

whittle()
for _ in range(20):
    clean()

my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))

out = 1
for name, val in zip(finals, my_ticket):
    if 'departure' in name:
        out *= val
        print('hit')

print(out)
