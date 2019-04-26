from graph import Graph
from networkx import *
# Find Strongly Connected Components using Kosaraju's algorithm
# Kosaraju's algorithm works as follows:
#
# Let G be a directed graph and S be an empty stack.
# While S does not contain all vertices:
#   Choose an arbitrary vertex v not in S.
#   Perform a depth-first search starting at v.
#   Each time that depth-first search finishes expanding a vertex u, push u onto S.
# Reverse the directions of all arcs to obtain the transpose graph.
# While S is nonempty:
#   Pop the top vertex v from S.
#   Perform a depth-first search starting at v in the transpose graph.
#   The set of visited vertices will give the strongly connected component containing v;
#   record this and remove all these vertices from the graph G and the stack S.

# Depth first search with postorder append to stack


def dfs(g, u, stack, explored):
    explored[u] = 1
    if u in g.graph_dict:
        for v in g.graph_dict[u]:
            if not explored[v]:
                dfs(g, v, stack, explored)
    stack.append(u)


def scc(g):
    explored = dict.fromkeys(g.graph_dict.keys(), 0)
    results = []
    # Initial DFS on G
    search_stack = []
    for v, expl in explored.items():
        if not expl and v != list(explored.keys())[0]:
            dfs(g, v, search_stack, explored)

    # Reverse Graph
    gr = g.reverse()
    exploredr = dict.fromkeys(g.graph_dict.keys(), 0)
    # DFS ordered by search_stack
    while len(search_stack) > 0:
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
    g1 = DiGraph(read_gexf("vk-friends-164285180.gexf"))
    return (g1.subgraph(c) for c in weakly_connected_components(g1))
