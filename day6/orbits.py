from copy import deepcopy


class Orb:
    def __init__(self,
                 name=None,
                 parent=None,
                 children=None,):
        if children is None:
            children = list()
        self.name = name
        self.parent = parent
        self.children = children

    def search_for_object(self, name):
        node_queue = [self]
        while node_queue:
            current_node = node_queue.pop(0)
            if current_node.name == name:
                return current_node
            else:
                node_queue += current_node.children
        return None

    def tree_size(self):
        ts = 0
        node_queue = [self]
        while node_queue:
            current_node = node_queue.pop(0)
            ts += current_node.depth()
            node_queue += current_node.children
        return ts

    def depth(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.depth()


if __name__ == '__main__':

    source = 'input'
    branches = []
    with open(source) as f:
        for line in f:
            objs = line.strip('\n').split(')')
            parent = Orb(name=objs[0])
            child = Orb(name=objs[1], parent=parent)
            parent.children.append(child)
            branches.append(parent)

    # Clean up the branches list:
    while len(branches) > 1:
        o = branches.pop(0)
        for b in branches:
            o_parent = b.search_for_object(o.name)
            if o_parent:
                for c in o.children:
                    c.parent = o_parent
                o_parent.children += o.children
                break
        else:
            branches.append(o)

    orbit_map = branches[0]
    s = orbit_map.tree_size()
    print(s)

    # Compute the orbital transfers required:
    you = orbit_map.search_for_object('YOU')
    p = you.parent
    up = 0
    while p.search_for_object('SAN') is None:
        p = p.parent
        up += 1
    p_parent = p.parent
    p.parent = None
    s = p.search_for_object('SAN')
    down = s.depth() - 1

    print(up + down)

