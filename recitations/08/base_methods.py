class PriorityQueue:
    def __init__(self):
        self.A = []


    def insert(self, x):
        self.A.append(x)

    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError('pop from empty priority queue')

        # this whole script can be reused in another class which inherits from this one
        # if in the other class we some some come
        # ---------------
        # and call
        # super().delete_max()
        return self.A.pop()         


    @classmethod
    def sort(Queue, A):
        # This algorithm runs in n(T_insert() + T_delete_max()) time

        # empty priority Queue
        pq = Queue() 

        # The algorithm part of n . T_insert(x)
        # complexity will depend on T_insert(x)
        for x in A:
            pq.insert(x)

        # The algorihtm part of n . T_delete_max()
        # Complexity will depend on how T_delete_max() occurs
        out = [pq.delete_max() for _ in A]

        # O(n) - makes floor(n/2) swaps
        out.reverse()
        return out
