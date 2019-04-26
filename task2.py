from graph import Graph
import matplotlib.pyplot as plt
import networkx as nx


def do_task2():
    g = nx.read_adjlist("undir_graph.csv")
    d = dict(nx.degree(g, g.nodes))
    print(sorted(d.items(), key=lambda x: x[1], reverse=True))
    print("Average vertex degree:", sum(d.values())/len(d))
    print("Diameter:", nx.diameter(g))
    print("Radius:", nx.radius(g))
    print("Center:", nx.center(g))
    print("Periphery:", nx.periphery(g))
    print("Average path length:", nx.average_shortest_path_length(g))

    degrees = {}
    for node in g.nodes():
        if g.degree(node) in degrees:
            degrees[g.degree(node)] += 1
        else:
            degrees[g.degree(node)] = 1
    plt.hist(degrees.keys(), bins=max(degrees.keys()), weights=[i / len(g.nodes()) for i in degrees.values()],
             rwidth=0.8, align='left')
    plt.xlabel("Vertex degree")
    plt.ylabel("Probability")
    plt.savefig("hist.png")
