from collections import defaultdict, deque
import random as rnd


# graph is matrix
def empty_graph(n, emp=0):
    """Makes an empty graph of with n nodes"""
    G = []
    for i in range(n):
        G += [[emp for _ in range(n)]]
    return G

def copy_graph(G):
    """Copies graph G"""
    n = len(G)
    G_ = empty_graph(n)
    for i, ei in enumerate(G):
        for j, e in enumerate(ei):
            G_[i][j] = e
    return G_

def undirected(G, t, mfunc=lambda:rnd.randint(0,9)):
    """Makes empty graph G undirected, adding t edges"""
    n = len(G)
    for i in range(t):
        k,l = rnd.randint(0,n-1), rnd.randint(0,n-1)
        m = mfunc()
        if k != l:
            G[k][l] = m
            G[l][k] = m

def directed(G, t, mfunc=lambda:rnd.randint(0,9)):
    """Makes empty graph G directed, adding t edges"""
    n = len(G)
    for i in range(t):
        k,l = rnd.randint(0,n-1), rnd.randint(0,n-1)
        m = mfunc()
        if k != l:
            G[k][l] = m

def undirected_to_directed(G):
    """Makes a undirected graph G, directed"""
    n = len(G)
    for i in range(n):
        for j in range(i+1, n):
            G[i][j] = 0
    return G

def DFS(G, s, visited=defaultdict(lambda: False)):
    """Depth First Search, on graph G, starts at node s.
        Returns a dictionary that tells whether that node is reachable from s."""
    visited[s] = True
    for i, e in enumerate(G[s]):
        if visited[i] == False and e != 0:
            DFS(G, i, visited)
    return visited

def BFS(G, s):
    """Breadth First Search, on graph G, starts at node s.
        Returns a dictionary that tells whether that node is reachable from s."""
    visited = defaultdict(lambda: False)
    visited[s] = True
    l = [s]
    while l: # exits when l is empty
        li = []
        for v in l:
            for w,_ in enumerate(G[v]):
                if visited[w] == False and G[v][w] == 1:
                    visited[w] = True
                    li += [w]
        l = li
    return visited

def deg_in(G, n):
    """Nodes going into node n"""
    indegree = 0
    for gi in G:
        indegree += gi[n]
    return indegree

def topological_sorting(G):
    """Topological sorts graph G"""
    S = deque()
    in_count = defaultdict(lambda: 0)
    for v, _ in enumerate(G):
        in_count[v] = deg_in(G, v)
        if in_count[v] == 0:
            S.append(v)
    i = 1
    output = []
    while len(S) != 0:
        v = S.popleft()
        output += [v]
        i += 1
        for w, e in enumerate(G[v]):
            if e == 1:
                in_count[w] -= 1
                if in_count[w] == 0:
                    S.append(w)
    if i > len(G):
        return output
    return "G has a cycle"

def str_graph(G):
    """Returns string of G"""
    return "\n".join([" ".join([str(gij) for gij in gi]) for gi in G])

def graph_to_list(G):
    """Makes a list based on graph G. On form (from, to, weight)."""
    A = []
    for v, e1 in enumerate(G):
        for u, m in enumerate(e1):
            if m != 0:
                A += [(v, u, m)]
    return A

def list_to_graph(A, n, t=""):
    """Makes a graph based on list A and number of nodes n. If undirected, make t='u'."""
    G = empty_graph(n)
    for u, v, m in A:
        G[u][v] = m
        if t == 'u':
            G[v][u] = m
    return G

def __main__():
    G = empty_graph(10)
    directed(G, 10, lambda:1)
    print(f"Directed graph G:\n{str_graph(G)}")
    print(f"DFS on G:\n{dict(DFS(G, 0))}")
    print(f"BFS on G:\n{dict(BFS(G, 0))}")
    print(f"Topological sorting of G:\n{topological_sorting(G)}")
    print(f"List form of G:\n{graph_to_list(G)}")

if __name__ == "__main__":
    __main__()
