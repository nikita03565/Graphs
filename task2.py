from graph import Graph
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter
from distance import diameter, radius, center, periphery, average_shortest_path_length


def do_task2():
    print("Task 2")
    g = nx.read_gexf("data/undir_graph.gexf")
    d = dict(nx.degree(g, g.nodes))
    print(sorted(d.items(), key=lambda x: x[1], reverse=True))
    print("Average vertex degree:", sum(d.values())/len(d))
    print("Diameter:", diameter(g))
    print("Radius:", radius(g))
    print("Center:", center(g))
    print("Periphery:", periphery(g))
    print("Average path length:", average_shortest_path_length(g))

    degrees = sorted([d for n, d in g.degree()], reverse=True)
    degrees = Counter(degrees)
    plt.hist(degrees.keys(), bins=max(degrees.keys()), weights=[i / len(g.nodes()) for i in degrees.values()], rwidth=0.9)
    plt.xlabel("Vertex degree")
    plt.ylabel("Probability")
    plt.savefig("outputs/hist.png")


if __name__ == "__main__":
    do_task2()
