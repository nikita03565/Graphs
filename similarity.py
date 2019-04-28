from math import log


def common_neighbors(g, u, v):
    return set(g[u]) & set(g[v])


def jaccard_coefficient(g, u, v):
    union_size = len(set(g[u]) | set(g[v]))
    if union_size == 0:
        return 0
    return len(set(g[u]) & set(g[v])) / union_size


def adamic_adar_index(g, u, v):
    return sum(1 / log(g.degree(w)) for w in set(g[u]) & set(g[v]))


def preferential_attachment(g, u, v):
    return g.degree(u) * g.degree(v)


def plain_bfs_undirected(g, source):
    g_adj = g.adj
    seen = set()
    nextlevel = {source}
    while nextlevel:
        thislevel = nextlevel
        nextlevel = set()
        for v in thislevel:
            if v not in seen:
                yield v
                seen.add(v)
                nextlevel.update(g_adj[v])
