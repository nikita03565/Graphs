class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def get_dict(self):
        return self.graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges_directed(self):
        return self.__generate_edges_directed()

    def edges_undirected(self):
        return self.__generate_edges_undirected()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def __generate_edges_directed(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                edges.append((vertex, neighbour))
        return edges

    def __generate_edges_undirected(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def reverse(self):
        graph = {}
        for i, j_list in self.graph_dict.items():
            for j in j_list:
                if j not in graph:
                    graph[j] = []
                graph[j].append(i)
        return Graph(graph)

    def read_adj_list(self, filename):
        with open(filename) as file:
            for line in file:
                x, y = line.split(sep=",")
                y = y.split()
                self.graph_dict[x] = y

    def vertex_degree(self, vertex):
        adj_vertices = self.graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def degree_sequence(self):
        seq = []
        for vertex in self.graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    @staticmethod
    def is_degree_sequence(sequence):
        return all(x >= y for x, y in zip(sequence, sequence[1:]))

    def delta(self):
        minimum = 100000000
        for vertex in self.graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < minimum:
                minimum = vertex_degree
        return minimum

    def Delta(self):
        maximum = 0
        for vertex in self.graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > maximum:
                maximum = vertex_degree
        return maximum

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return path

    def diameter(self):
        v = self.vertices()
        pairs = [(v[i], v[j]) for i in range(len(v)) for j in range(i + 1, len(v) - 1)]
        smallest_paths = []
        for (s, e) in pairs:
            paths = self.find_all_paths(s, e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        diameter = len(smallest_paths[-1]) - 1
        return diameter

    def to_undirected(self):
        graph = Graph()
        vert = self.vertices()
        edges = self.edges_undirected()
        for v in vert:
            graph.add_vertex(v)
        for e in edges:
            graph.add_edge(e)
        return graph

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges_directed():
            res += str(edge) + " "
        return res
