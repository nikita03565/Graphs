def degree_centrality(g):
    if len(g) <= 1:
        return {n: 1 for n in g}

    centrality = {n: d / (len(g) - 1.0) for n, d in g.degree()}
    return centrality


def closeness_centrality(g, v):
    pass


def eigenvector_centrality(g, v):
    pass


def betweenness_centrality(g, v):
    pass


def edge_betweenness(g, v):
    pass
