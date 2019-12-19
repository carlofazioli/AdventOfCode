import string
from math import factorial, exp
import numpy as np
import random
from concurrent.futures import ProcessPoolExecutor, as_completed


class Maze:
    def __init__(self,
                 source_file=None):
        with open(source_file) as f:
            maze = [list(line.rstrip('\r\n')) for line in f]
        self.width = len(maze[0])
        self.height = len(maze)
        self.maze = dict()
        self.doors = dict()
        self.keys = dict()
        self.entrance = None
        self.reachable = dict()
        for x in range(self.width):
            for y in range(self.height):
                self.maze[(x, y)] = maze[y][x]
                if maze[y][x] in string.ascii_lowercase:
                    self.keys[maze[y][x]] = (x, y)
                if maze[y][x] in string.ascii_uppercase:
                    self.doors[maze[y][x]] = (x, y)
                if maze[y][x] == '@':
                    self.entrance = (x, y)

    def unlock(self, key):
        if self.doors.get(key.upper()):
            self.maze[self.doors[key.upper()]] = ' '
        self.maze[self.keys[key]] = ' '

    def lock(self):
        for door in self.doors:
            self.maze[self.doors[door]] = door
        for key in self.keys:
            self.maze[self.keys[key]] = key

    def build_graph(self):
        graph = dict()
        for i in range(self.width):
            for j in range(self.height):
                if self.maze[(i, j)] in string.ascii_lowercase + ' @':
                    graph[(i, j)] = set()
        for v in graph:
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

    def reachable_keys(self, unlock_path):
        reachable_keys = self.reachable.get(unlock_path, set())
        if reachable_keys:
            return reachable_keys
        m.lock()
        for key in unlock_path:
            m.unlock(key)
        boundary = set()
        if len(unlock_path) > 0:
            source = self.keys[unlock_path[-1]]
        else:
            source = self.entrance
        boundary.add(source)
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
                            reachable_keys.add(maze_char)
        self.reachable[unlock_path] = reachable_keys
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

        if source is None:
            source = self.entrance
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


def augment_path(source_file, current_path, target_key):
    # This is for parallelization
    m = Maze(source_file)
    for key in current_path:
        m.unlock(key)
    source = m.keys[current_path[-1]]
    target = m.keys[target_key]
    d, _ = m.dijkstra(source=source, target=target)
    return target_key, d


def build_cost_matrix(maze):
    for key in maze.keys:
        maze.unlock(key)
    pairs = dict()
    for k1 in sorted(maze.keys):
        for k2 in sorted(maze.keys):
            if k1 == k2:
                source = None
            else:
                source = maze.keys[k1]
            d, _ = maze.dijkstra(source=source, target=maze.keys[k2])
            pairs[(k1, k2)] = d
    return pairs


def valid_path(path, maze):
    for i in range(len(path)):
        ch = path[i]
        pre_path = path[:i]
        valid = maze.reachable_keys(pre_path)
        if ch not in valid:
            return False
    return True


def path_cost(path, pairs, maze):
    if valid_path(path, maze):
        if path:
            cost = pairs[(path[0], path[0])]
            for a, b in zip(path[:-1], path[1:]):
                cost += pairs[tuple(sorted([a, b]))]
            return cost
        else:
            return 0
    else:
        return float('infinity')


def build_candidate(maze, pairs):
    paths = sorted(maze.reachable_keys(''), key=lambda x: pairs[(x, x)])
    candidate = paths[0]
    while len(candidate) < len(maze.keys):
        paths = sorted(maze.reachable_keys(candidate), key=lambda x: pairs[tuple(sorted([candidate[-1], x]))])
        candidate += paths[0]
    return candidate


class Node:
    def __init__(self,
                 parent=None,
                 key=None):
        self.parent = parent
        self.key = key
        self.path = self.get_path()

    def get_path(self):
        if self.parent:
            return self.parent.get_path() + self.key
        else:
            return self.key


if __name__ == '__main__':

    source_file = 'test4'
    m = Maze(source_file)

    cost_pairs = build_cost_matrix(m)
    best_candidate = build_candidate(m, cost_pairs)
    best_bound = path_cost(best_candidate, cost_pairs, maze=m)
    annealing_candidate = str(best_candidate)
    annealing_bound = best_bound

    print('candidate solution: ', best_candidate)
    print('candidate bound: ', best_bound)

    # Simulated annealing:
    # n_annealing_steps = 10000
    # steps_completed = 0
    # for t in np.logspace(0, 5, n_annealing_steps)[::-1]:
    #     if steps_completed % (n_annealing_steps//10) == 0:
    #         print('{}% complete'.format(100*steps_completed/n_annealing_steps))
    #     i, j = sorted(random.sample(range(len(m.keys)), 2))
    #     candidate = best_candidate[:i] + best_candidate[j] + best_candidate[i + 1:j] + best_candidate[i] + best_candidate[j + 1:]
    #     cost_candidate = path_cost(candidate, cost_pairs, m)
    #     if exp((annealing_bound - cost_candidate) / t) > random.random():
    #         annealing_candidate = candidate
    #         annealing_bound = cost_candidate
    #     if cost_candidate < best_bound:
    #         best_candidate = candidate
    #         best_bound = cost_candidate
    #     steps_completed += 1
    #
    # print('Simulated Annealing done...')
    # print(best_candidate)
    # print(best_bound)


    n_search_space = factorial(len(m.keys))
    print('estimated search space: ', n_search_space)
    init_node = Node(key='')
    init_paths = sorted(m.reachable_keys(init_node.get_path()), key=lambda x: cost_pairs[(x, x)])
    queue = []
    for p in init_paths:
        queue.append(Node(parent=init_node, key=p))
    paths_analyzed = 0
    while queue:
        node = queue.pop(0)
        node_path = node.get_path()
        cost = path_cost(path=node_path, pairs=cost_pairs, maze=m)
        if len(node_path) == len(m.keys):
            if cost < best_bound:
                print('updating bound: {} -> {}'.format(best_bound, cost))
                best_bound = cost
                best_candidate = node_path
        elif cost < best_bound:
            ordered_paths = sorted(m.reachable_keys(node_path), key=lambda x: cost_pairs[tuple(sorted([node_path[-1],
                                                                                                    x]))])
            for k in ordered_paths:
                queue.append(Node(parent=node, key=k))
        paths_analyzed += 1
        if paths_analyzed % 10000 == 0:
            print('{} paths analyzed - estimated {}\% complete'.format(paths_analyzed, paths_analyzed / n_search_space))

    print('new solution: ', best_candidate)
    print('new bound: ', best_bound)

    #
    # paths = {p: pairs[(p, p)] for p in m.reachable_keys('')}
    #
    # updates = dict()
    # # for p, d in paths.items():
    #
    # # Greedily build out paths:
    # sorted_paths = sorted(paths, key=lambda x: paths[x])
    # shortest_path = sorted_paths[0]
    # shortest_dist = paths.pop(shortest_path)
    #
    # while len(shortest_path) < len(m.keys):
    #     print('shortest path:', shortest_path)
    #     print('shortest dist:', shortest_dist)
    #
    #     last_key = shortest_path[-1]
    #     for key in m.reachable_keys(shortest_path):
    #         d = pairs[tuple(sorted([last_key, key]))]
    #         new_path = shortest_path + key
    #         paths[new_path] = shortest_dist + d
    #
    #
    #     # with ProcessPoolExecutor(max_workers=26) as executor:
    #     #     futures = [executor.submit(augment_path, source_file, shortest_path, key)
    #     #                for key in remaining_keys]
    #     #     results = [f.result() for f in futures]
    #     # for key, d in results:
    #     #     if d < float('infinity'):
    #     #         new_path = shortest_path + key
    #     #         all_paths[new_path] = shortest_dist + d
    #     sorted_paths = sorted(paths, key=lambda x: paths[x])
    #     shortest_path = sorted_paths[0]
    #     shortest_dist = paths.pop(shortest_path)
    #
    # print('shortest path:', shortest_path)
    # print('shortest dist:', shortest_dist)
