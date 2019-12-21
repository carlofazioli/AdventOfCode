import string


class Maze:
    def __init__(self,
                 source_file=None):
        # Reads the source file in a list of lists:
        with open(source_file) as f:
            maze = [list(line.rstrip('\r\n')) for line in f]
        # Stores the maze dimensions:
        self.width = len(maze[0])
        self.height = len(maze)
        # The maze, doors, and keys are all stored as dictionaries:
        self.maze = dict()
        self.doors = dict()
        self.keys = dict()  # Including the maze entrance
        self.key_locs = dict()
        # The sorted string of reachable maze keys, from a given point and set of obtained maze keys; i.e. the dict
        # keys looks like (x, y, 'stringofkeys')
        self.reachable = dict()
        # Here we parse the maze list-of-list to populate our dicts:
        for x in range(self.width):
            for y in range(self.height):
                self.maze[(x, y)] = maze[y][x]
                if maze[y][x] in string.ascii_lowercase + '@':
                    self.keys[maze[y][x]] = (x, y)
                    self.key_locs[(x, y)] = maze[y][x]
                if maze[y][x] in string.ascii_uppercase:
                    self.doors[maze[y][x]] = (x, y)
        # Here we use Dijkstra to find the pairwise distances between maze keys:
        for key in self.keys:
            self.unlock(key)
        self.pairs = dict()
        sorted_keys = sorted(self.keys)
        n = len(sorted_keys)
        for i in range(n):
            for j in range(i, n):
                k1 = sorted_keys[i]
                k2 = sorted_keys[j]
                print('Computing Dijkstra dist: ', k1, k2)
                if i == j:
                    self.pairs[(k1, k2)] = 0
                else:
                    start, finish = sorted([k1, k2])
                    d, _ = self.dijkstra(source=self.keys[start], target=self.keys[finish])
                    self.pairs[(k1, k2)] = d
        self.lock()
        self.scores = dict()

    def build_graph(self):
        # This builds the graph of the maze in its current state; i.e. with any doors locked.
        # It populates the graph with unreachable locations, but Dijkstra will come back with their dist as inf.
        #
        # The keys are valid locations.  The values of those keys are the neighbors.
        graph = dict()
        for i in range(self.width):
            for j in range(self.height):
                # Valid locations are empty, and those with maze keys.
                # The dict values are sets who will be populated with the location's neighbors.
                if self.maze[(i, j)] in list(self.keys.keys()) + [' ']:
                    graph[(i, j)] = set()
        for v in graph:
            # For each valid location, add its neighbors:
            x, y = v
            if (x+1, y) in graph:
                graph[v].add((x+1, y))
            if (x-1, y) in graph:
                graph[v].add((x-1, y))
            if (x, y+1) in graph:
                graph[v].add((x, y+1))
            if (x, y-1) in graph:
                graph[v].add((x, y-1))
        return graph

    def unlock(self, key):
        # We've stored all the x,y locations of the doors.
        # The keys are the door name (e.g. 'A', 'R'), and the value is x,y location.
        # To unlock a door is to replace it with a space; this allows the build_graph() to connect the two regions.
        # Also, replace the key itself with a space.
        if self.doors.get(key.upper()):
            self.maze[self.doors[key.upper()]] = ' '
        self.maze[self.keys[key]] = ' '

    def lock(self):
        # We've stored all the x,y locations of the doors.
        # The keys are the door name (e.g. 'A', 'R'), and the value is x,y location.
        # To lock the doors means to put them all back in place. Also put the keys back in place.
        for door in self.doors:
            self.maze[self.doors[door]] = door
        for key in self.keys:
            self.maze[self.keys[key]] = key

    def reachable_keys(self, x, y, obtained_keys):
        # This is a typical flood fill algorithm in the current maze state (i.e. some doors unlocked), from the given
        # state.

        # First check the maze's set of previously known reachable keys:
        obtained_keys = ''.join(sorted(obtained_keys))
        reachable_keys = self.reachable.get((x, y, obtained_keys), '')
        if reachable_keys:
            return reachable_keys

        # If ya don't got it, ya gotta compute it.
        # Lock all the doors, then unlock the ones you've got.  Now the maze state reflects the current obtained_keys.
        m.lock()
        for key in obtained_keys:
            m.unlock(key)

        # Carry out the flood fill:
        boundary = set()
        boundary.add((x, y))
        interior = set()
        while boundary:
            loc = boundary.pop()
            interior.add(loc)
            x, y = loc
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for n in neighbors:
                if n not in interior:
                    maze_char = self.maze.get(n)
                    if maze_char in [' ', '@'] + list(self.keys.keys()):
                        boundary.add(n)
                        if maze_char in list(self.keys.keys()):
                            reachable_keys += maze_char
                            reachable_keys = sorted(reachable_keys)

        # Make sure we add all that nice hard work to the dict:
        self.reachable[(x, y, obtained_keys)] = reachable_keys
        return reachable_keys

    def display(self, source=None, target=None):
        if not source and not target:
            for y in range(self.height):
                row = []
                for x in range(self.width):
                    row.append(self.maze[(x, y)])
                print(''.join(row))

    def dijkstra(self, source=None, target=None):

        def min_dist(vertices, distances):
            d = float('infinity')
            v = None
            for vert in vertices:
                if distances[vert] < d:
                    v = vert
            return v if v is not None else vert

        current_graph = self.build_graph()
        q = dict(current_graph)
        dist = dict()
        prev = dict()
        for vertex in q:
            dist[vertex] = float('infinity')
            prev[vertex] = None
        dist[source] = 0

        while q:
            u = min_dist(q, dist)
            if u == target:
                break
            q.pop(u)
            for neighbor in current_graph[u]:
                d_neighbor = dist[u] + 1
                if d_neighbor < dist[neighbor]:
                    dist[neighbor] = d_neighbor
                    prev[neighbor] = u

        path = []
        dist = dist[target]
        if prev[target] or target == source:
            while target:
                path.insert(0, target)
                target = prev[target]

        return dist, path

    def score(self, current_key, obtained_keys):
        if current_key in obtained_keys:
            return 0
        if self.scores.get((current_key, obtained_keys)):
            return self.scores[(current_key, obtained_keys)]
        x, y = self.keys[current_key]
        reach = self.reachable_keys(x, y, obtained_keys)
        recurse = []
        for key in reach:
            new_obtained_keys = ''.join(sorted(list(set(obtained_keys) | set(key))))
            tmp = self.score(key, new_obtained_keys)
            tmp += self.pairs[tuple(sorted([current_key, key]))]
            recurse.append(tmp)
        if len(recurse) == 0:
            val = 0
        else:
            val = min(recurse)
        print('Updating score to obtain {} from {}: '.format(current_key, obtained_keys))
        self.scores[(current_key, obtained_keys)] = val
        return val



if __name__ == '__main__':

    source_file = 'input'
    m = Maze(source_file)
    print('moving on...')
    print(m.score('', ''))

    input()

