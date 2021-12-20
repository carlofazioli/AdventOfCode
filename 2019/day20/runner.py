from collections import defaultdict
from string import ascii_uppercase
from dijkstra import Graph


class WarpMaze:
    def __init__(self,
                 source_file=None):
        with open(source_file) as f:
            maze = [list(line.strip('\r\n')) for line in f]
        self.width = max([len(row) for row in maze])
        self.height = len(maze)
        self.loc_warp = dict()
        self.warp_loc = defaultdict(set)
        self.graph = Graph()
        self.interior = set()
        self.exterior = set()

        # Copy the file to the local dict:
        self.maze = self.copy_to_dict(maze)

        # Identify all the wormhole tokens:
        self.parse_warps()

        # Populate graph:
        self.build_graph()

        # Start/finish for the maze:
        self.source = self.warp_loc['AA'].pop()
        self.target = self.warp_loc['ZZ'].pop()

        # Part 2:
        self.scores = dict()

    def copy_to_dict(self, list_of_lists):
        maze_dict = dict()
        for y, row in enumerate(list_of_lists):
            for x, ch in enumerate(row):
                maze_dict[(x, y)] = ch
        return maze_dict

    def parse_warps(self):
        for x in range(self.width):
            for y in range(self.height):
                ch_1 = self.maze.get((x, y), ' ')
                t_x = None
                t_y = None
                # If ch_1 is the start of a token identifier may have found a token:
                if ch_1 in ascii_uppercase:
                    # These are the horizontal tokens:
                    ch_2 = self.maze.get((x + 1, y), ' ')
                    if ch_2 in ascii_uppercase:
                        if self.maze.get((x + 2, y)) == '.':
                            t_x = x + 2
                        if self.maze.get((x - 1, y)) == '.':
                            t_x = x - 1
                        self.loc_warp[(t_x, y)] = ch_1 + ch_2
                    ch_2 = self.maze.get((x - 1, y), ' ')
                    if ch_2 in ascii_uppercase:
                        if self.maze.get((x - 2, y)) == '.':
                            t_x = x - 2
                        if self.maze.get((x + 1, y)) == '.':
                            t_x = x + 1
                        self.loc_warp[(t_x, y)] = ch_2 + ch_1

                    # These are vertical tokens:
                    ch_2 = self.maze.get((x, y + 1), ' ')
                    if ch_2 in ascii_uppercase:
                        if self.maze.get((x, y + 2)) == '.':
                            t_y = y + 2
                        if self.maze.get((x, y - 1)) == '.':
                            t_y = y - 1
                        self.loc_warp[(x, t_y)] = ch_1 + ch_2
                    ch_2 = self.maze.get((x, y - 1), ' ')
                    if ch_2 in ascii_uppercase:
                        if self.maze.get((x, y - 2)) == '.':
                            t_y = y - 2
                        if self.maze.get((x, y + 1)) == '.':
                            t_y = y + 1
                        self.loc_warp[(x, t_y)] = ch_2 + ch_1
        for loc, warp in self.loc_warp.items():
            self.warp_loc[warp].add(loc)
            x, y = loc
            if 2 < x < self.width - 3 and 2 < y < self.height -3:
                self.interior.add(loc)
            else:
                self.exterior.add(loc)

    def flood_fill(self, warp):
        def neighbors(x, y):
            return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for loc in self.warp_loc[warp]:
            boundary = [loc]
            interior = []
            flood_dist = 0
            while boundary:
                flood_dist += 1
                b_size = len(boundary)
                for _ in range(b_size):
                    b = boundary.pop(0)
                    interior.append(b)
                    hood = neighbors(*b)
                    for n_xy in hood:
                        if n_xy in self.loc_warp and n_xy != loc:
                            self.graph.add([loc, n_xy, flood_dist])
                            interior.append(n_xy)
                        if self.maze.get(n_xy) == '.' and n_xy not in boundary and n_xy not in interior:
                            boundary.append(n_xy)

    def build_graph(self):
        for warp, locs in self.warp_loc.items():
            if len(locs) > 1:
                n1 = locs.pop()
                n2 = locs.pop()
                self.graph.add([n1, n2, 1])
                locs.add(n1)
                locs.add(n2)
            self.flood_fill(warp)

    def maze_solve(self):
        dist, path = self.graph.dijkstra(self.source, self.target)
        named_path = []
        for graph_node in path:
            named_path.append(self.loc_warp[graph_node])
        return dist, named_path

    def min_cost_to_exit(self, state):
        if state == (*self.target, 0):
            return 0
        if state in self.scores:
            return self.scores[state]







if __name__ == '__main__':

    warp_maze = WarpMaze('input')
    d, p = warp_maze.maze_solve()
    print('dist: ', d)
    print('path: ', p)
    print()

    input()



