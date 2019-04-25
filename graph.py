from networkx import strongly_connected_components, weakly_connected_components


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                #if {neighbour, vertex} not in edges:
                edges.append({vertex, neighbour})
        return edges

    def read_adj_list(self, filename):
        with open(filename) as file:
            for line in file:
                x, *y = line.split()
                #print(x, y)
                self.__graph_dict[x] = y

    def get_strongly_connected_components_iterative(self):
        """
        This is a non-recursive version of strongly_connected_components_path.
        See the docstring of that function for more details.

        Examples
        --------
        Example from Gabow's paper [1]_.

        >>> vertices = [1, 2, 3, 4, 5, 6]
        >>> edges = {1: [2, 3], 2: [3, 4], 3: [], 4: [3, 5], 5: [2, 6], 6: [3, 4]}
        >>> for scc in strongly_connected_components_iterative(vertices, edges):
        ...     print(scc)
        ...
        set([3])
        set([2, 4, 5, 6])
        set([1])

        Example from Tarjan's paper [2]_.

        >>> vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        >>> edges = {1: [2], 2: [3, 8], 3: [4, 7], 4: [5],
        ...          5: [3, 6], 6: [], 7: [4, 6], 8: [1, 7]}
        >>> for scc in  strongly_connected_components_iterative(vertices, edges):
        ...     print(scc)
        ...
        set([6])
        set([3, 4, 5, 7])
        set([8, 1, 2])

        """
        identified = set()
        stack = []
        index = {}
        boundaries = []

        for v in self.__graph_dict.keys():
            if v not in index:
                to_do = [('VISIT', v)]
                while to_do:
                    operation_type, v = to_do.pop()
                    if operation_type == 'VISIT':
                        index[v] = len(stack)
                        stack.append(v)
                        boundaries.append(index[v])
                        to_do.append(('POSTVISIT', v))
                        # We reverse to keep the search order identical to that of
                        # the recursive code;  the reversal is not necessary for
                        # correctness, and can be omitted.
                        to_do.extend(
                            reversed([('VISITEDGE', w) for w in self.__graph_dict[v]]))
                    elif operation_type == 'VISITEDGE':
                        if v not in index:
                            to_do.append(('VISIT', v))
                        elif v not in identified:
                            while index[v] < boundaries[-1]:
                                boundaries.pop()
                    else:
                        # operation_type == 'POSTVISIT'
                        if boundaries[-1] == index[v]:
                            boundaries.pop()
                            scc = set(stack[index[v]:])
                            del stack[index[v]:]
                            identified.update(scc)
                            yield scc

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
