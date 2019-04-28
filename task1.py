from graph import Graph
from component import wcc, scc


def do_task1():
    print("Task 1")
    g = Graph()
    g.read_adj_list(filename="data/graph_list.csv")

    results = [sorted(result) for result in scc(g)]
    results.sort(key=lambda result: result[0])
    print("Number of strongly connected components: ", len(results))
    print("Count, Percantage, Component")
    for result in results:
        print(len(result), "(" + str(len(result)/len(g.vertices()) * 100.0) + "%)", result)

    cc = [c for c in wcc(g)]
    results = [sorted(result) for result in cc]
    results.sort(key=lambda result: result[0])
    print("Number of weakly connected components: ", len(results))
    print("Count, Percantage, Component")
    for result in results:
        print(len(result), "(" + str(len(result)/len(g.vertices()) * 100.0) + "%)", result)


if __name__ == "__main__":
    do_task1()
