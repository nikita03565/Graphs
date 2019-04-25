from graph import Graph
from component import scc

g = Graph()
g.read_adj_list(filename="graph_list.csv")

results = [sorted(result) for result in scc(g)]
results.sort(key=lambda result: result[0])
print("Number of strongly connected components: ", len(results))
print("Count, Percantage, Component")
for result in results:
    print(len(result), "(", len(result)/len(g.vertices()) * 100.0, " %)", result)

