""" Implementation of Heap Sort """

def max_heapify(seq, i, n):
    l = i + 1
    r = i + 2

    if l <= n and seq[l] > seq[i]:
        largest = l
    else:
        largest = i
    if r <= n and seq[r] > seq[largest]:
        largest = r
    
    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        max_heapify(seq, largest, n)


def build_heap(seq):
    n = len(seq) - 1
    for i in range(n, -1, -1):
        max_heapify(seq, i, n)

def sort(seq):
    build_heap(seq)
    heap_size = len(seq) - 1
    for x in range(heap_size, -1, -1):
        seq[0], seq[x] = seq[x], seq[0]
        heap_size = heap_size - 1
        max_heapify(seq, 0, heap_size)
    
    return seq
