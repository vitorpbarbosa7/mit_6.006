

class E:
    def __init__(self, key):
        self.key = key

        
class Obj:
    def __init__(self):

        # The digits that will serve for the tuple sort part
        self.digits = None
        
        self.item = None
        
        # the new keys
        self.key = None

def counting_sort(A): # A: List[Obj]
 
    # O(n) find maximum key of A
    u = 1 + max([x.key for x in A]) 

    # O(u) initialize the chains in each position of Direct Access Array - DAA
    DAA = [[] for i in range(u)]

    # O(n) inserto into each chain of DAA, according to their key
    # invariant or order preserved to be a stable sorting algorithm
    for x in A:
        DAA[x.key].append(x)

    # Sorting part
    # 
    i = 0
    for chain in DAA:
        for element in chain:
            A[i] = element
            i += 1


def radix_sort(A): # A: List[Obj]
    "Sort A assuming A has non-negative keys"

    n = len(A)

    # O(n) find max in A (n elements in total)
    u = 1 + max([x.key for x in A])

    # as the logn(u), just getting how much elements are needed to represent the number u in base n
    c = 1 + (u.bit_length() // n.bit_length())

    D = [Obj() for x in A]

    # O(nc) make digit tuples
    # O(n) because we will traverse each item in A
    # c because we will for each item in A (n items) create a tuple of length c 
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key

        # O(c) for each of the keys, make the digit tuple
        for j in range(c):
            high, low = divmod(high, n)
            D[i].digits.append(low)
    
    # imagine the tuple will be of length two
    # the first time it will assign to the D list the key equals to D[j].digits[0], that is, the element from the tuple which is index 0 (least significant algorithm)
    # the second time it will assignt the the D list the key equals to D[j].digits[1], that is, the element from the tuple which is index 1 (more significant algorithm)
    for i in range(c):
        # for all elements 
        for j in range(n): 
            D[j].key = D[j].digits[i]
        counting_sort(D)
    
    for i in range(n):
        A[i] = D[i].item

    return A


def sort_string(T):
    hashord = {ord(s): s for s in T}
    elements = [ord(s) for s in T]

    A = [E(x) for x in elements]

    print('Unsorted: ', [x.key for x in A])

    Asorted = radix_sort(A)

    print('Sorted:', [x.key for x in Asorted])

    sorted_string = ''
    for sorted_item in Asorted:
        ch = hashord[sorted_item.key]

        sorted_string += ch

    return sorted_string

T = 'eslea'




        


