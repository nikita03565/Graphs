from math import log


def common_neighbours(g, u, v):
    return set(g[u]) & set(g[v])


def jaccard_coefficient(g, u, v):
    union = set(g[u]) | set(g[v])
    intersection = set(g[u]) & set(g[v])
    if not union:
        return 0
    return len(intersection) / len(union)


def adamic_adar_index(g, u, v):
    return sum(1 / log(g.degree(w)) for w in set(g[u]) & set(g[v]))


def preferential_attachment(g, u, v):
    return g.degree(u) * g.degree(v)
