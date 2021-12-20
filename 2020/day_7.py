import utilities


rules = utilities.input_to_list('day_7.txt')


def get_container_color(r):
    idx = r.find('bags')
    color = r[:idx-1]
    contents = r[idx+13:]
    return color, contents


def get_contents_color(contents):
    start = contents.index(' ') + 1
    end = contents.index('bag') - 1
    return contents[start:end]


def get_contents_colors(contents):
    con = contents.split(', ')
    if len(con) == 1 and 'no other' in con[0]:
        return []
    return [get_contents_color(c) for c in con]


color_map = {}


def parse_rule(r):
    container_color, contents_raw = get_container_color(r)
    if container_color not in color_map:
        color_map[container_color] = set()
    contents_colors = get_contents_colors(contents_raw)
    for color in contents_colors:
        if color not in color_map:
            color_map[color] = set()
        color_map[color].add(container_color)


def solve_part_1():
    for rule in rules:
        parse_rule(rule)

    s = color_map['shiny gold']
    checked = set()
    while s:
        color = s.pop()
        checked.add(color)
        s.update(color_map[color])

    return len(checked)


contents_map = {}


def get_contents_count(c):
    idx = c.index(' ')
    return int(c[:idx])


def parse_contents(contents_raw):
    contents = contents_raw.split(', ')
    if len(contents) == 1 and 'no other' in contents[0]:
        return [(0, '')]
    counts = [get_contents_count(c) for c in contents]
    colors = [get_contents_color(c) for c in contents]
    return zip(counts, colors)


def parse_rule_2(r):
    container_color, contents_raw = get_container_color(r)
    if container_color not in contents_map:
        contents_map[container_color] = set()
    contents = parse_contents(contents_raw)
    contents_map[container_color].update(set(contents))


def count(color):
    if color == '':
        return 0
    contents = contents_map[color]
    return sum(c[0]*(1 + count(c[1])) for c in contents)


def solve_part_2():
    for rule in rules:
        parse_rule_2(rule)
    return count('shiny gold')

print(solve_part_1())
print(solve_part_2())
input()