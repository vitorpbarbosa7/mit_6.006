class E:
    def __init__(self, key):
        self.key = key

def counting_sort(A):

    # O(n) find maximum key of A
    u = 1 + max([x.key for x in A]) 

    # O(u) initialize the chains in each position of Direct Access Array - DAA
    DAA = [[] for i in range(u)]

    # O(n) insert into each chain of DAA, according to their key
    # invariant or order preserved to be a stable sorting algorithm
    for x in A:
        DAA[x.key].append(x)

    # Sorting part
    # 
    i = 0
    for chain in DAA:
        for element in chain:
            # get the elements into A in sorted order
            # since it was inserted in sorted order
            A[i] = element
            i += 1

# Example usage
elements = [17,3,24,22,12] 
A = [E(x) for x in elements]

print("Unsorted:", [x.key for x in A])

counting_sort(A)

print("Sorted:", [x.key for x in A])
