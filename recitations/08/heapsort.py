'''
Now let's take advantage of the logarithmic height of a complete binary tree (balanced) to improve performance. 
The perfomance will be improved since the insertion and deletion will take at most the height of the tree to 
traverse it using the heapify_up() and heapify_down() methods, which in this case are max ones 
using the max_heapify_up() and max_heapify_down() calls
'''

from elementkey import E
from inplaceheaps import PriorityQueue
from binary_heap_helpers import (
    max_heapify_down,
    max_heapify_up
)

#TODO
# use the build in linear time 

class PQHeap(PriorityQueue):

    def insert(self, *args):

        # basically using the base method for insertion
        # and after making arragements for keeping the Max Heap Property
        super().insert(*args)

        # after the initial insertion, it will be incorrect, it will not 
        # satisfy the condition of a Complete Binary Tree
        # and so hot have the Max Heap Property Invariant

        # let's fix it

        # A is just a pointer to self.A, so this occurs all inplace
        n, A = self.n, self.A
        max_heapify_up(A, n, n-1)

    def delete_max(self):

        print(self.n)

        n, A = self.n-1, self.A

        # the very simple way to delete max swapping 
        # the first element (root) with last element (most right leaf)
        A[0], A[n] = A[n], A[0]
        max_heapify_down(A, n, 0)

        return super().delete_max()

# Example Usage:

if __name__ == '__main__':

    X = [8, 1, 3, 9, 6, 7, 4, 5]
    elements = [E(x) for x in X]

    sorted = PQHeap.sort(elements)
    print(sorted)
