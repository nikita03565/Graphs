def single_source_shortest_path_length(G, source, cutoff=None):
    if cutoff is None:
        cutoff = float('inf')
    nextlevel = {source: 1}
    return dict(single_shortest_path_length(G.adj, nextlevel, cutoff))


def single_shortest_path_length(adj, firstlevel, cutoff):
    seen = {}
    level = 0
    nextlevel = firstlevel

    while nextlevel and cutoff >= level:
        thislevel = nextlevel
        nextlevel = {}
        for v in thislevel:
            if v not in seen:
                seen[v] = level
                nextlevel.update(adj[v])
                yield (v, level)
        level += 1
    del seen


def eccentricity(G, v=None, sp=None):
    e = {}
    for n in G.nbunch_iter(v):
        if sp is None:
            length = single_source_shortest_path_length(G, n)
        else:
            length = sp[n]

        e[n] = max(length.values())

    if v in G:
        return e[v]
    else:
        return e


def diameter(G, e=None):
    if e is None:
        e = eccentricity(G)
    return max(e.values())


def periphery(G, e=None):
    if e is None:
        e = eccentricity(G)
    diameter = max(e.values())
    p = [v for v in e if e[v] == diameter]
    return p


def radius(G, e=None):
    if e is None:
        e = eccentricity(G)
    return min(e.values())


def center(G, e=None):
    if e is None:
        e = eccentricity(G)
    radius = min(e.values())
    p = [v for v in e if e[v] == radius]
    return p


def average_shortest_path_length(G):
    n = G.order()
    s = sum(l for u in G for l in single_source_shortest_path_length(G, u).values())
    return s / (n * (n - 1))
