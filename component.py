from networkx import read_gexf


def dfs(g, u, stack, explored):
    explored[u] = 1
    if u in g.graph_dict:
        for v in g.graph_dict[u]:
            if not explored[v]:
                dfs(g, v, stack, explored)
    stack.append(u)


def plain_bfs_directed(g, u):
    gsucc = g.succ
    gpred = g.pred

    seen = set()
    nextlevel = {u}
    while nextlevel:
        thislevel = nextlevel
        nextlevel = set()
        for v in thislevel:
            if v not in seen:
                yield v
                seen.add(v)
                nextlevel.update(gsucc[v])
                nextlevel.update(gpred[v])
                
                
def scc(g):
    explored = dict.fromkeys(g.graph_dict.keys(), 0)
    results = []
    # Initial DFS on g
    search_stack = []
    for v, expl in explored.items():
        if not expl and v != list(explored.keys())[0]:
            dfs(g, v, search_stack, explored)

    # Reverse graph
    gr = g.reverse()
    exploredr = dict.fromkeys(g.graph_dict.keys(), 0)
    # DFS ordered by search_stack
    while search_stack:
        u = search_stack[-1]
        scc_stack = []
        dfs(gr, u, scc_stack, exploredr)
        for v in scc_stack:
            if v in gr.graph_dict:
                del gr.graph_dict[v]
            search_stack.remove(v)
        results.append(scc_stack)
    return results


def wcc(g):
    g = read_gexf("data/vk-friends-164285180.gexf")
    seen = set()
    for v in g:
        if v not in seen:
            c = set(plain_bfs_directed(g, v))
            yield c
            seen.update(c)
