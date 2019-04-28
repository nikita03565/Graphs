import networkx as nx
from similarity import common_neighbors, jaccard_coefficient, adamic_adar_index, preferential_attachment


def do_task3():
    print("Task 3")
    graph = nx.read_gexf("data/undir_graph.gexf")
    x, y = list(graph)[4], list(graph)[17]

    print(len(common_neighbors(graph, x, y)))
    print(jaccard_coefficient(graph, x, y))
    print(adamic_adar_index(graph, x, y))
    print(preferential_attachment(graph, x, y))


if __name__ == "__main__":
    do_task3()
