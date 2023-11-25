from elementkey import E
from priorityqueueinterface import PriorityQueue

class PQSortedArray(PriorityQueue):
    # in this case, for a Sorted Dynamic Array, the delete_max is already correct
    # because we know that the maximum element key will be in the last position

    # So if we depend upon the delete_max always poping up the bigger element 
    # the array must be sorted, that is what we will code now 

    def insert(self, *args):
        super().insert(*args)

        i, A = len(self.A) - 1, self.A
        
        while i > 0 and A[i - 1].key > A[i].key:
            # swap them, because the previous element is bigger than the next element 
            A[i - 1], A[i] = A[i], A[i - 1]
            i -= 1

            # breakpoint()


# Example Usage

if __name__ == '__main__':

    X = [4,2,7,6,8,1,2,3,1,5,78,5,2]
    elements = [E(x) for x in X]

    sorted = PQSortedArray().sort(elements)
    print(sorted)
