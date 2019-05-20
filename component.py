from networkx import read_gexf


def dfs(g, u, stack, explored):
    explored[u] = 1
    if u in g.graph_dict:
        for v in g.graph_dict[u]:
            if not explored[v]:
                dfs(g, v, stack, explored)
    stack.append(u)


def bfs(g, u):
    seen = set()
    next = {u}
    while next:
        cur = next
        next = set()
        for v in cur:
            if v not in seen:
                yield v
                seen.add(v)
                next.update(g.succ[v])
                next.update(g.pred[v])
                
                
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
            c = set(bfs(g, v))
            yield c
            seen.update(c)
