from day14.reactions import parse_elements, parse_token
import parse
import sympy
import numpy as np


def build_equations(source):
    reaction_form = '{} => {}'
    ore_requirements = {}
    table_of_elements = set()
    eqs = []
    with open(source) as f:
        for line in f:
            reaction = list(parse.parse(reaction_form, line))

            lhs = reaction[0]
            rhs = reaction[1]
            rhs_n, rhs_name = parse_token(rhs)
            table_of_elements.add(rhs_name)

            eq = {}
            for reactant in lhs.split(','):
                n, name = parse_token(reactant)
                if name == 'ore':
                    ore_requirements[rhs_name] = {n: rhs_n}
                    table_of_elements.add(rhs_name)
                    break
                table_of_elements.add(name)
                eq[name] = n
            if eq:
                eq[rhs_name] = -rhs_n
                eqs.append(eq)
    table_of_elements = sorted(table_of_elements)
    table_of_elements.remove('fuel')
    table_of_elements.append('fuel')
    return table_of_elements, eqs, ore_requirements


def convert_eqs(eqs, table_of_elements):
    formatted = []
    while eqs:
        eq = eqs.pop()
        row = []
        for key in table_of_elements:
            row.append(eq.get(key, 0))
        formatted.append(row)
    return formatted


toe, eqs, ores = build_equations('test2')
eqs = convert_eqs(eqs, toe)

lcm = 1
for row in eqs:
    for val in row:
        if val != 0:
            lcm = np.lcm(lcm, val)

colsum = [0] * len(eqs[0])
for row in eqs:
    for i in range(len(eqs[0])):
        colsum[i] += row[i]/lcm

# gcd = 0
# for val in colsum:
#     if val != 0:
#         gcd = np.gcd(gcd, val)

for i in range(len(colsum)):
    colsum[i] *= lcm


# m = np.array(eqs)
# x = np.linalg.lstsq(m, np.zeros((4, 1)))
mat = sympy.Matrix(eqs)
mrref = mat.rref()
print(mrref)
input()

