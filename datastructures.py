import numpy as np
import random as rnd

class Node():
    """Binary tree"""

    def __init__(self, symbol, freq, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def __le__(self, other):
        return self.freq < other.freq

    def __str__(self):
        return self.main_str()

    def main_str(self, tb=0):
        """Creates a string representation of tree"""
        l,r = "",""
        if self.left != None:
            l = self.left.main_str(tb+1)
        if self.right != None:
            r = self.right.main_str(tb+1)
        return "| "*tb + str(self.symbol) + ", " + str(self.freq) +"\n"+ l + r

# Heaps
def insert(A, x):
    """Inserts element x on heap A"""
    n = len(A)
    A += [x]
    i = n
    while 0 < i and A[i] < A[(i - 1)//2]:
        A[i], A[(i - 1)//2] = A[(i - 1)//2], A[i]
        i = (i - 1)//2
    return A

def remove_min(A):
    """Removes the minimum element in heap A"""
    x = A[0]
    n = len(A)
    A[0] = A[n - 1]
    i = 0
    while 2*i + 2 < n - 1:
        j = 2*i + 1 if A[2*i + 1] <= A[2*i + 2] else 2*i + 2
        if A[j] <= A[i]:
            A[i], A[j] = A[j], A[i]
            i = j
            continue
        break
    if 2*i + 1 < n - 1 and A[2*i + 1] <= A[i]:
        A[i], A[2*i + 1] = A[2*i + 1], A[i]
    return A[:-1], x

def huffman(C):
    """Creates a Huffman tree"""
    Q = []
    for p in C:
        s,f = p
        Q = insert(Q, Node(s, f, None, None))
    while len(Q) > 1:
        Q, v1 = remove_min(Q)
        Q, v2 = remove_min(Q)
        Q = insert(Q, Node(v1.symbol + v2.symbol, v1.freq + v2.freq, v1, v2))
    return remove_min(Q)[1]

def __main__():
    # Heap
    A = [int(rnd.random()*100)]
    for i in range(5):
        n = int(rnd.random()*100)
        insert(A, n)
    print(f"Heap A:{A}")
    A, x = remove_min(A)
    print(f"Remove element of heap A:\n x = {x}, A = {A}")

    # Huffman
    C = []
    for l in "abcdefghijklmnopqrstuvwxyz":
        C += [(l, int(rnd.random()*100))]
    h = huffman(C)
    print(f"\nHuffman:\n{h}")

if __name__ == "__main__":
    __main__()
