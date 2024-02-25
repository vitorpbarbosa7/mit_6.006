

class E:
    def __init__(self, key = None):
        self.key = key
        # The digits that will serve for the tuple sort part
        self.digits = None
        self.item = None

    def __str__(self):
        return f'''\nkey: {self.key} - digits: {self. digits} - item: {self.item}'''
    
    def __repr__(self):
        return self.__str__()

def counting_sort(A): # A: List[Obj]

    print('Input of counting Sort')    
    print(A)
    breakpoint()
    
 
    # O(n) find maximum key of A
    u = 1 + max([x.key for x in A]) 

    # O(u) initialize the chains in each position of Direct Access Array - DAA
    # the chains are necessary to keep the order in which the items were put there
    # preserving previous ordres from least significant sorting make previously 
    # allowing for an algorithm which will for each pass, be stable 
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

# The tuple sort uses each pass of the direct access array sort (modified to be stable with the chaining, which make us call it a counting sort)
def radix_sort(A): # A: List[Obj]
    "Sort A assuming A has non-negative keys"

    n = len(A)

    # O(n) find max in A (n elements in total)
    u = 1 + max([x.key for x in A])

    # as the logn(u), just getting how much elements are needed to represent the number u in base n
    c = 1 + (u.bit_length() // n.bit_length())

    D = [E() for x in A]

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
    # the first time it will assign to the D list the key equals to D[j].digits[0], that is, the element from the tuple which is index 0 (least significant digit)
    # the second time it will assignt the D list the key equals to D[j].digits[1], that is, the element from the tuple which is index 1 (more significant digit)
            
    # apply the couting sort (modified direct acess sort) for each of the digits, which represent the general number in the n base 
    # that is why we used the divmod(k, n) for each k in n, as max(A[n]) = u, and u might be u >> n
    for i in range(c):
        # for all elements 
        for j in range(n): 
            D[j].key = D[j].digits[i]
        # using the counting sort (modified direct acess array sort to be stable)
        counting_sort(D)
        # so D is being sorted the current significant digit (which is assigned to the key) is asked for, and the item it self (original number) 
        # the digits (least to most significant, we have stored before in the looping with divmod)
        # will be following this sorting sequence
    
    for i in range(n):
        A[i] = D[i].item

    return A
    
# Example usage
elements = [17,3,24,22,12] 
A = [E(x) for x in elements]

print('Unsorted: ', [x.key for x in A])

Asorted = radix_sort(A)

print('Sorted:', [x.key for x in Asorted])


        


