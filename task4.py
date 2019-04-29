from centrality import degree_centrality
from networkx import read_gexf
import csv


def do_task4():
    g = read_gexf("data/undir_graph.gexf")
    dc = degree_centrality(g)
    with open('outputs/degree_centrality.csv', mode='w') as dc_file:
        dc_file = csv.writer(dc_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for vertex, value in dc.items():
            dc_file.writerow([vertex, value])


if __name__ == "__main__":
    do_task4()
