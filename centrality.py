from distance import single_source_shortest_path_length


def degree_centrality(g):
    if len(g) <= 1:
        return {v: 1 for v in g}

    degree = {v: d / (len(g) - 1.0) for v, d in g.degree()}
    return degree


def closeness_centrality(g):
    closeness = {v: (len(g)-1.0)/sum(single_source_shortest_path_length(g, v).values()) for v in g.nodes}
    return closeness


def eigenvector_centrality(g, v):
    pass


def betweenness_centrality(g, v):
    pass


def edge_betweenness(g, v):
    pass
