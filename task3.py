import networkx as nx
from similarity import common_neighbours, jaccard_coefficient, adamic_adar_index, preferential_attachment
import csv


def do_task3():
    print("Task 3")
    graph = nx.read_gexf("data/undir_graph.gexf")

    nodes = graph.nodes
    with open('outputs/neighbors.csv', mode='w') as neighbors_file:
        neighbors_file = csv.writer(neighbors_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        neighbors_file.writerow([None] + list(nodes))
        for x in nodes:
            neighbors_file.writerow([x] + [len(common_neighbours(graph, x, y)) if x is not y else '' for y in nodes])

    with open('outputs/jaccard.csv', mode='w') as jaccard_file:
        jaccard_file = csv.writer(jaccard_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        jaccard_file.writerow([None] + list(nodes))
        for x in nodes:
            jaccard_file.writerow([x] + [jaccard_coefficient(graph, x, y) if x is not y else '' for y in nodes])
            
    with open('outputs/adamic.csv', mode='w') as adamic_file:
        adamic_file = csv.writer(adamic_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        adamic_file.writerow([None] + list(nodes))
        for x in nodes:
            adamic_file.writerow([x] + [adamic_adar_index(graph, x, y) if x is not y else '' for y in nodes])
            
    with open('outputs/preferential.csv', mode='w') as pref_file:
        pref_file = csv.writer(pref_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        pref_file.writerow([None] + list(nodes))
        for x in nodes:
            pref_file.writerow([x] + [preferential_attachment(graph, x, y) if x is not y else '' for y in nodes])


if __name__ == "__main__":
    do_task3()
