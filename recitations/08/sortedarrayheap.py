from elementkey import E
from base_methods import PriorityQueue

class PQSortedArray(PriorityQueue):
    # in this case, for a Sorted Dynamic Array, the delete_max is already correct
    # because we know that the maximum element key will be in the last position

    # So if we depend upon the delete_max always poping up the bigger element 
    # the array must be sorted, that is what we will code now 

    def insert(self, *args):
        super().insert(*args)

        i, A = len(self.A) - 2, self.A
        
        while i > 0 and A[i].key > A[i + 1].key:
            # swap them, because the previous element is bigger than the next element 
            A[i + 1], A[i] = A[i], A[i + 1]
            i -= 1


# Example Usage

if __name__ == '__main__':

    X = [4,6,2,4,7,8,1,6,7]
    elements = [E(x) for x in X]

    sorted = PQSortedArray().sort(elements)
    print(sorted)
