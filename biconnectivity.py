import random as rnd
from graphs import *
from collections import defaultdict

def graph_without_vertex(G, v):
    """Returns G without vertex v"""
    G_ = []
    for u, e1 in enumerate(G):
        if u != v:
            G_ += [e1[:v] + e1[v+1:]]
    return G_

def connected(G):
    """Checks if G is connected"""
    for v in G:
        if sum(v) == 0:
            return False
    return True

def biconnectivity(G):
    """Checks for biconnectivity for G.
    If some node can be removed for G to not be connected, G is not bicconected.
    Returns the nodes that can be removed to make G not connected"""
    sep_vertices = []
    for v,_ in enumerate(G):
        G_ = graph_without_vertex(G, v)
        if connected(G_) == False:
            sep_vertices += [v]
    return sep_vertices

def hopcroft_tarjan(G, u, depth):
    """Uses Hopcroft-Tarjan algorythm to return seperation nodes"""
    visited = defaultdict(lambda:False)
    low = {}
    index = {}
    def hopcroft_tarjan1(G, u, depth, sep_vertices=[]):
        visited[u] = True
        low[u] = index[u] = depth
        child_count = 0
        for v, e in enumerate(G[u]):
            if e != 0:
                if visited[v] == False:
                    child_count += 1
                    hopcroft_tarjan1(G, v, depth+1, sep_vertices)
                    low[u] = min(low[u], low[v])
                    if index[u] != 1:
                        if index[u] <= low[v]:
                            sep_vertices += [u]
                else:
                    low[u] = min(low[u], index[v])
        if index[u] == 1:
            if child_count > 1:
                sep_vertices += [u]
        return sep_vertices
    return hopcroft_tarjan1(G, u, depth)

def __main__():
    n = 10
    G = empty_graph(n, 0)
    undirected(G, 20, lambda:1)
    print(f"Graph G:\n{str_graph(G)}")
    print(f"Biconnectivity:\n{biconnectivity(G)}")
    print(f"Hopcroft-Tarjan:\n{hopcroft_tarjan(G,0,0)}")

if __name__ == "__main__":
    __main__()
