from graph import Graph
from networkx import DiGraph, read_gexf
# Find Strongly Connected Components using Kosaraju's algorithm
# Kosaraju's algorithm works as follows:
#
# Let g be a directed graph and S be an empty stack.
# While S does not contain all vertices:
#   Choose an arbitrary vertex v not in S.
#   Perform a depth-first search starting at v.
#   Each time that depth-first search finishes expanding a vertex u, push u onto S.
# Reverse the directions of all arcs to obtain the transpose graph.
# While S is nonempty:
#   Pop the top vertex v from S.
#   Perform a depth-first search starting at v in the transpose graph.
#   The set of visited vertices will give the strongly connected component containing v;
#   record this and remove all these vertices from the graph g and the stack S.

# Depth first search with postorder append to stack


def dfs(g, u, stack, explored):
    explored[u] = 1
    if u in g.graph_dict:
        for v in g.graph_dict[u]:
            if not explored[v]:
                dfs(g, v, stack, explored)
    stack.append(u)


def plain_bfs_directed(g, source):
    gsucc = g.succ
    gpred = g.pred

    seen = set()
    nextlevel = {source}
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
    while len(search_stack):
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
    g = DiGraph(read_gexf("data/vk-friends-164285180.gexf"))
    seen = set()
    for v in g:
        if v not in seen:
            c = set(plain_bfs_directed(g, v))
            yield c
            seen.update(c)
