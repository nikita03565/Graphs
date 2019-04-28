def single_source_shortest_path_length(g, source, cutoff=None):
    if cutoff is None:
        cutoff = float('inf')
    nextlevel = {source: 1}
    return dict(single_shortest_path_length(g.adj, nextlevel, cutoff))


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


def eccentricity(g, v=None, sp=None):
    e = {}
    for n in g.nbunch_iter(v):
        if sp is None:
            length = single_source_shortest_path_length(g, n)
        else:
            length = sp[n]

        e[n] = max(length.values())

    if v in g:
        return e[v]
    else:
        return e


def diameter(g, e=None):
    if e is None:
        e = eccentricity(g)
    return max(e.values())


def periphery(g, e=None):
    if e is None:
        e = eccentricity(g)
    diameter = max(e.values())
    p = [v for v in e if e[v] == diameter]
    return p


def radius(g, e=None):
    if e is None:
        e = eccentricity(g)
    return min(e.values())


def center(g, e=None):
    if e is None:
        e = eccentricity(g)
    radius = min(e.values())
    p = [v for v in e if e[v] == radius]
    return p


def average_shortest_path_length(g):
    n = g.order()
    s = sum(l for u in g for l in single_source_shortest_path_length(g, u).values())
    return s / (n * (n - 1))
