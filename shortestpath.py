import numpy as np
import random as rnd
from graphs import *
import sorting as srt

class Node():
    def __init__(self, n, v):
        self.n = n
        self.v = v

    def __str__(self):
        return str(self.n)

    def __gt__(self, other):
        return self.n > other.n

def remove_min(A):
    """Removes the smallest element in a sorted list A"""
    e = A[0]
    return A[1:], e

def dijkstra(G,s):
    """In undirected graph G, finds the shortest path length from s to all other nodes using Djikstra"""
    Q = []
    D = {}
    for u,_ in enumerate(G):
        D[u] = Node(np.inf, u)
        Q += [D[u]]
    D[s].n = 0
    srt.insertion_sort(Q)
    while Q != []:
        Q,v = remove_min(Q)
        for t, m in enumerate(G[v.v]):
            if m != 0:
                if Node(D[v.v].n + m, -1) < D[t]:
                    D[t] = Node(D[v.v].n + m, v.v)
                    srt.insertion_sort(Q)
    return {i: D[i].n for i in D}

def bellman_ford(G, s):
    """In directed graph G, finds the shortest path length from s to all other nodes using Bellman-Ford"""
    D = {}
    for u,_ in enumerate(G):
        D[u] = Node(np.inf, u)
    D[s] = Node(0, s)
    Ga = graph_to_list(G)
    for i in range(1, len(G)):
        for u,v,m in Ga:
            if Node(D[u].n + m, -1) < D[v]:
                D[v].n = D[u].n + m
    for u,v,m in Ga:
        if Node(D[u].n + m, -1) < D[v]:
            return "G has a negative cycle"
    return {i: D[i].n for i in D}

def __main__():
    n = 10
    G = empty_graph(n, 0)
    undirected(G, 15)
    print(f"Graph g:\n{str_graph(G)}")
    print(f"Djikstra:\n{dijkstra(G, 0)}")

    G = empty_graph(n, 0)
    directed(G, 25)
    print(f"Graph g:\n{str_graph(G)}")
    print(f"Bellman-Ford:\n{bellman_ford(G, 0)}")

if __name__ == "__main__":
    __main__()
