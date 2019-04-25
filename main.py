from graph import Graph

g = Graph()
g.read_adj_list(filename="graph_list.csv")

scc = g.get_strongly_connected_components_iterative()
for s in scc:
    print(len(s), s)

