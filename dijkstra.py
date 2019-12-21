from collections import defaultdict


class Graph:
    def __init__(self,
                 connections=[],
                 directed=False):
        self.nodes = defaultdict(set)
        self.edges = defaultdict(int)
        self.directed = directed

        # Populate the initial set of connections:
        for connection in connections:
            self.add(connection)

    def add(self, connection):
        """ A connection is a (potentially ordered) list of 2 nodes/states. """
        n1 = connection[0]
        n2 = connection[1]
        w = connection[2] if len(connection) == 3 else 0

        # Add the nodes in their given, assumed-directed order; also add the other order
        # if graph undirected.  Similarly for the edges.
        self.nodes[n1].add(n2)
        if not self.directed:
            self.nodes[n2].add(n1)
            edge = tuple(sorted([n1, n2]))
        else:
            edge = (n1, n2)
        self.edges[edge] = w

    def dijkstra(self,
                 source=None,
                 dest=None):
        """
        Uses Dijkstra's Algorithm to find the shortest path between the source and distination
        nodes of the given graph.
        """

        def minimum_distance_node():
            d = float('infinity')
            n = None
            for queue_node in priority_queue:
                if node_distances[queue_node] < d:
                    d = node_distances[queue_node]
                    n = queue_node
            return n

        # Initialize data structures:
        priority_queue = dict.fromkeys(self.nodes.keys())
        explored = []
        node_distances = dict()
        node_previous = dict()
        for node in priority_queue:
            node_distances[node] = float('infinity')
            node_previous[node] = None
        node_distances[source] = 0

        # Dijkstra's Algorithm:
        while priority_queue:
            u = minimum_distance_node()
            priority_queue.pop(u)
            if u == dest:
                continue
            for neighbor in self.nodes[u]:
                edge_key = [u, neighbor]
                if not self.directed:
                    edge_key = sorted(edge_key)
                edge_length = self.edges[tuple(edge_key)]
                if node_distances[u] + edge_length < node_distances[neighbor]:
                    node_distances[neighbor] = node_distances[u] + edge_length
                    node_previous[neighbor] = u

        shortest_path = [dest]
        shortest_dist = node_distances[dest]
        while node_previous[dest]:
            shortest_path.insert(0, node_previous[dest])
            dest = node_previous[dest]

        return shortest_dist, shortest_path











