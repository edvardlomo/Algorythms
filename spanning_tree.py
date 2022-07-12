import random as rnd
import numpy as np
from graphs import *


def prim(G):
    """Finds minimum spanning tree from G"""
    v = 0
    D = {}
    D[v] = [[v, None], 0]
    T, Q = [], []
    for u,_ in enumerate(G):
        if u != v:
            D[u] = [[u, None], np.inf]
        Q += [D[u]]
    while Q != []:
        u, e = Q[0]
        Q = Q[1:]
        if u[1] != None:
            T += [(u[0], u[1], e)]
        for z, m in enumerate(G[u[0]]):
            if m < D[z][1] and m != 0:
                D[z][0] = [z,u[0]]
                D[z][1] = m
    return list_to_graph(T, len(G), 'u')

def kruskal(G):
    """Finds minimum spanning tree from G"""
    T = []
    G = copy_graph(G)
    Q = graph_to_list(undirected_to_directed(G))
    Q.sort(key=lambda a: a[2])
    C = {}
    for v,_ in enumerate(G):
        C[v] = {v}
    while len(T) < len(G) - 1:
        u,v,m = Q[0]
        Q = Q[1:]
        if C[u] != C[v]:
            T += [(u,v,m)]
            C_ = C[u].union(C[v])
            for z in C[u]:
                C[z] = C_
            for z in C[v]:
                C[z] = C_
    return list_to_graph(T, len(G), 'u')

def __main__():
    n = 5
    G = empty_graph(n)
    undirected(G, 1000)
    print(f"Graph G:\n{str_graph(G)}")
    print(f"Prim:\n{str_graph(prim(G))}")
    print(f"Kruskal:\n{str_graph(kruskal(G))}")

if __name__ == "__main__":
    __main__()
