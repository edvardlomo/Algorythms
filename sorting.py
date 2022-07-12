def bubble_sort(A):
    """Does bubble sort on list A"""
    n = len(A)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

def selection_sort(A):
    """Does selection sort on list A"""
    n = len(A)
    for i in range(0, n):
        k = i
        for j in range(i + 1, n):
            if A[j] < A[k]:
                k = j
        if i != k:
            A[i], A[k] = A[k], A[i]

def insertion_sort(A):
    """Does insertion sort on list A"""
    n = len(A)
    for i in range(0, n):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1

def __main__():
    import random as rn
    S = [rn.randint(0, 100) for i in range(10)]
    def print_sort(Sorter, symbol):
        A = S.copy()
        Sorter(A)
        print(symbol, A)

    print_sort(bubble_sort, "BS: ")
    print_sort(selection_sort, "SS: ")
    print_sort(insertion_sort, "IS: ")


if __name__ == "__main__":
    __main__()
