class E:
    def __init__(self, key):
        self.key = key

def counting_sort(A):
    u = 1 + max([x.key for x in A])
    D = [[] for _ in range(u)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1

# Example usage
elements = [3,1,4,1,2,4] 
A = [E(x) for x in elements]

print("Unsorted:", [x.key for x in A])

counting_sort(A)

print("Sorted:", [x.key for x in A])
