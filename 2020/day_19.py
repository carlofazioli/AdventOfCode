import utilities


example = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

with open('input_files/day_19.txt') as f:
    raw = f.read().strip()
rules_raw, messages_raw = raw.split('\n\n')
# rules_raw, messages_raw = example.strip().split('\n\n')

rules = dict()
for rule in rules_raw.split('\n'):
    name, val = rule.split(':')
    val = val.strip()
    if val == '"a"' or val == '"b"':
        ch = val[1]
        rules[int(name)] = ch
        continue
    val = val.split('|')
    rules[int(name)] = [list(map(int, v.strip().split(' '))) for v in val]


messages = messages_raw.split('\n')


def match(rules_dict, s, rule_index, s_index):
    # Use the rules_dict to match validate string s against rule_dict[rule_index], at s_index.
    # If index is beyond string len, cannot match:
    if s_index >= len(s):
        return []

    # Get the current rule:
    rule = rules_dict[rule_index]

    # If the current rule is a string literal, match against it and advance the s_index:
    if isinstance(rule, str):
        if s[s_index] == rule:
            return [s_index+1]
        else:
            return []

    matches = []
    # If the rule is a not a string literal, then it is a list of 1 or more lists of options.
    for option in rule:
        sub_matches = [s_index]
        for subrule in option:
            new_matches = []
            for idx in sub_matches:
                new_matches += match(rules_dict, s, subrule, idx)
            sub_matches = new_matches
        matches += sub_matches
    return matches


valid = 0
for s in messages:
    valid += len(s) in match(rules, s, 0, 0)

# Part 2
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

valid2 = 0
for s in messages:
    valid2 += len(s) in match(rules, s, 0, 0)