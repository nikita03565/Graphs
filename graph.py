from networkx import strongly_connected_components, weakly_connected_components


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a directed graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def get_dict(self):
        return self.graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graph_dict.keys())

    def edges_direcred(self):
        """ returns the edges of a graph """
        return self.__generate_edges_directed()

    def edges_undirecred(self):
        """ returns the edges of a graph """
        return self.__generate_edges_undirected()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def __generate_edges_directed(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                edges.append([vertex, neighbour])
        return edges

    def __generate_edges_undirected(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    # Reverses the directed edges of a graph, returning a new graph
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
                x, *y = line.split()
                #print(x, y)
                self.graph_dict[x] = y

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges_directed():
            res += str(edge) + " "
        return res
