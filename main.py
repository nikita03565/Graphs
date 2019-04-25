from graph import Graph
from component import scc

g = Graph()
g.read_adj_list(filename="graph_list.csv")
'''scc = g.get_strongly_connected_components_iterative()
for s in scc:
    print(len(s), s)'''
#print(g)
#g1 = g.reverse()
#print(g)
results = [sorted(result) for result in scc(g)]
results.sort(key=lambda result: result[0])
print(len(results))
for result in results:
    print (len(result), result)
