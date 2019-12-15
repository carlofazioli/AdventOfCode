import parse
from math import ceil


def parse_token(t):
    t = t.split(' ')
    return int(t[-2]), t[-1].lower()


def parse_elements(source):
    reaction_form = '{} => {}\n'
    table_of_elements = {'ore': Element(data={'name': 'ore',
                                              'requires': dict(),
                                              'group_size': 1,
                                              'is_required_by': dict()})}
    with open(source) as f:
        for line in f:
            # Parse line for reaction equation:
            reaction_equation = list(parse.parse(reaction_form, line))

            # Create new element for RHS:
            n_produced, name = parse_token(reaction_equation[1])
            table_of_elements[name] = Element(data={'name': name,
                                                    'requires': dict(),
                                                    'group_size': n_produced,
                                                    'is_required_by': dict()})
            for reactant in reaction_equation[0].split(','):
                n_required, requirement_name = parse_token(reactant)
                table_of_elements[name].data['requires'][requirement_name] = n_required
    return table_of_elements


class Element:
    def __init__(self,
                 data=None):
        self.requires = set()
        self.used_by = set()
        self.data = data

    def ore_requirements(self):
        ore = 0
        for elem in self.used_by:
            req = self.total_required()
            group_size = elem.data['group_size']
            groups_req = ceil(req / group_size)
            group_cost = self.data['is_required_by'][elem.data['name']]
            ore += groups_req * group_cost
        return ore

    def total_required(self):
        req = 0
        for k, v in self.data['is_required_by'].items():
            req += v
        return req

    def link_dependencies(self, table_of_elements):
        ratio = ceil(self.total_required() / self.data['group_size'])
        for elem_name, n_required in self.data['requires'].items():
            self.requires.add(table_of_elements[elem_name])
            table_of_elements[elem_name].used_by.add(self)
            table_of_elements[elem_name].data['is_required_by'][self.data['name']] = n_required * ratio
        for elem_name in self.requires:
            elem_name.link_dependencies(table_of_elements)


if __name__ == '__main__':
    tril = 1000000000000
    N = 2595246
    table_of_elements = parse_elements('input')
    fuel = table_of_elements['fuel']
    fuel.data['is_required_by']['self'] = N
    fuel.link_dependencies(table_of_elements)
    ore = table_of_elements['ore']
    req = sum(list(ore.data['is_required_by'].values()))
    print(req)
    print(tril)
