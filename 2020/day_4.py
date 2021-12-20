import utilities


with open(f'input_files/day_4.txt') as f:
    batch_raw = f.read()

passports = batch_raw.split('\n\n')

req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def process_passport(p):
    p = p.replace('\n', ' ')
    fields = p.split(' ')
    keys = [field.split(':')[0] for field in fields]
    for k in req_keys:
        if k not in keys:
            return False
    return True


def check_byr(y):
    return 1920 <= int(y) <= 2002


def check_iyr(y):
    return 2010 <= int(y) <= 2020


def check_eyr(y):
    return 2020 <= int(y) <= 2030


def check_hgt(h):
    if h[-2:] == 'cm':
        return 150 <= int(h[:-2]) <= 193
    if h[-2:] == 'in':
        return 59 <= int(h[:-2]) <= 76
    return False


def check_hcl(c):
    if c[0] == '#' and len(c) == 7:
        try:
            int(c[1:], 16)
            return True
        except ValueError:
            return False
    return False


def check_ecl(c):
    return c in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_pid(i):
    if len(i) == 9:
        try:
            int(i)
            return True
        except ValueError:
            return False
    return False


checks = {
    'byr': check_byr,
    'iyr': check_iyr,
    'eyr': check_eyr,
    'hgt': check_hgt,
    'hcl': check_hcl,
    'ecl': check_ecl,
    'pid': check_pid,
}


def process_passport_2(p):
    p = p.replace('\n', ' ')
    fields = p.split(' ')
    p_dict = dict(field.split(':') for field in fields)
    for k in req_keys:
        if k not in p_dict:
            return False
        if not checks[k](p_dict[k]):
            return False
    return True


def solve_part_2():
    return sum(process_passport_2(p) for p in passports)


def solve_part_1():
    return sum(process_passport(p) for p in passports)


print(solve_part_2())