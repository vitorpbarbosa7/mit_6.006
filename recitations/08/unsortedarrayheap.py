from base_methods import PriorityQueue
from elementkey import E

class PQArray(PriorityQueue):
    
    # For the logic of Selecion Sort, the basemethod which inserts at the end
    # is already correct, because this is not the case of a Sorted Array, but a common 
    # unsorted array
    # in which after the delete_max operation will take n to run, since it will traverse whole 
    # array in order to find the max value till now 
    # if we're finding the max value up to now
    # this makes clear how to PriorityQueue Interface along as with the Data Structure of Unsorted Array
    # and the idea of Priority Queue Sort, results in the same logic as the Selection Sort 
    # and this will run in O(n**2)-time 

    # Recalling that the Priority Queue Sorting Algorithm takes into account the following equation:
    # n(T_insert() + T_delete_max())

    def delete_max(self):
        print('\n', self.A)
        n, A, m = len(self.A)-1, self.A , 0
        print(n)

        for i in range(n+1):
            print(f'm and i: {A[m].key, A[i].key}')
            # breakpoint()
            if A[i].key > A[m].key:
                m = i

        print('max to be dropped', A[m])

        # once we found what is the item with max value (take the index)
        # swap the max with the end of the array 
        A[m], A[n] = A[n], A[m]

        # them return the last value, (that we shifted to the end of the array)
        
        # out super().delete_max() is the simple one programmed with pop
        return super().delete_max()

# Example Usage

if __name__ == '__main__':

    X = [4,2,7,6,8,1,2,3,1,5,78,5,2]
    elements = [E(x) for x in X]

    sortede = PQArray().sort(elements)
    print(sortede)
    print(sorted(X))
