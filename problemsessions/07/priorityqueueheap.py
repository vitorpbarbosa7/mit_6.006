class Item:
    def __init__(self, label, key):
        self.label = label
        self.key = key

class PriorityQueue:
    def __init__(self):
        # remember that a priority queue heap implementation uses a implicit data structure, that is 
        # a array, in which we do not have pointers, or references
        self.A = []
        # Another necessary data structure of a hash to use as cross linking to achieve
        # constant time look-up for each element in the heap by the distance to source vertex
        self.label2idx = {}

    def min_heapify_up(self, c):
        # c: child index in the array
        # p: parent index in the array
        if c == 0:
            return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:
            # the heapify up operation, swaping child and parent nodes
            self.A[c], self.A[p] = self.A[p], self.A[c]
            # update the hash
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            # recursive call to continue heapifying up to maintain the Heap Property Invariant
            self.min_heapify_up(p)

    def min_heapify_down(self, p):
        if p >= len(self.A):
            return
        # get left and right child according to the Heap way of doing that in the tree  
        l = 2 * p + 1
        r = 2 * p + 2
        if l >= len(self.A):
            l = p
        if r >= len(self.A):
            r = p
        # child is the smaller one, in the heapify min
        if self.A[r].key > self.A[l].key:
            c = l
        else:
            c = r
        
        if self.A[p].key > self.A[c].key:
            # Heapify down by swaping child and parent nodes
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)

    def insert(self, label, key):
        # amortized with this dynamic array list implementation of python
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        # keep the dict with the vertex label and the index (position in the array)
        self.label2idx[self.A[idx].label] = idx
        # insert at the bottom (max idx, last element of the array), so it has to heapify up this last item
        # as necessary, using the recursion inside min_heapify_up implementation 
        self.min_heapify_up(idx)

    def extract_min(self):
        # extract first element (root of the tree and first element of the array)
        # and heapify down after removal of last element (which is firstly swapped with first)

        # swap first element and last
        # to make possible to be easy to remove the min element whilch will be now last element 
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        
        del self.label2idx[self.A[-1].label]
        min_label = self.A.pop().label
        self.min_heapify_down(0)
        return min_label

    def decrease_key(self, label, key):
        '''
        label: node label
        key: distance from the source vertex
        '''
        # the part in which the cross linking will make the difference
        # to be able to access any vertex
        if label in self.label2idx: # O(1) hash
            # returning the distance
            idx = self.label2idx[label]
            # if new distance to the source vertex is less than current stored distance to source vertex, then update it 
            if key < self.A[idx].key:
                self.A[idx].key = key
                # we changed to a smaller distance, therefore this smaller distance may go up in the 
                # Min Heap, that is why we use a min_heapify_up
                self.min_heapify_up(idx)


