from binary_heap_helpers import build_max_heap 
from elementkey import E


X = [7, 3, 5, 6, 2, 0, 3, 1, 9, 4]
A = [E(x) for x in X]

A1 = A[:8]

# a)
# linear 
A2 = build_max_heap(A1)

# # b)
# # insert
# heap = PQHeap(A2)
# heap.insert(E(X[8]))
# heap.insert(E(X[9]))

# #c)
# heap.delete_max()
# heap.delete_max()