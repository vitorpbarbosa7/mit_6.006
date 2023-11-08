from numpy import array as arr

"""
Divide an conquer strategy, that is, splitting the list into two peaces (famous probably log2 complexity)

Steps:

1 - If list is of length 0 or 1, list is already sorted
2 - If list has more than one element, split into two lists, and sort each

The list is split in half until have sublists of only 1 element

 
3 - Merge sorted lists

3.1 - Look at first element of each, move smaller to first positions?
3.2 - When one list is empty, add all remaining element of the other list to the merged list
"""

"""
Complexity analysis of merge

go through two lists, only one pass

compare only the smallest elements in each sublist

O(len(left) + len(right)) copied elements
O(len(longer list)) comparisons
linear in lenght of the lists
"""


def merge(A, i, j, last_digit):

    temp = A.copy()

    """
    Merging two lists in a sorted manner, considering that each list is already sorted
    """
    print(f"merging {A[i:j]} and {A[j:last_digit+1]}")

    init_i = i
    j_limit = j

    print(f' #### pointers ####')
    print(f'left is {A[i]}')
    print(f'right is {A[j]}')
    print(f' left > right: {A[i]>A[j]}')

    internal_counter = init_i
    while i < j and j < last_digit:

        # if left is greater than j
        if temp[i] > temp[j]:
            A[internal_counter] = temp[j]
            j += 1
        else:
            A[internal_counter] = temp[i]
            # left is less than right, then left is already where it should be
            i += 1
        
        internal_counter += 1

    while i < j_limit:
        A[internal_counter] = temp[i]
        internal_counter += 1
        i += 1

    while j < last_digit:
        print(f'j is {j}')
        A[internal_counter] = temp[j]
        internal_counter += 1
        j += 1

    print(f"Result of merging: {A[init_i:last_digit+1]}\n")

    return A

def mergesort(A, i=0, j=None):

    """
    L : list of elements
    side: keep track of what side is it in
    """

    if j == None:
        j = len(A)

    last_digit = j-1

    print(
        f"""
	   Stack frame created 
	   List: {A[i:last_digit+1]}
    """
    )

    # Base Case
    if j - i < 2:
        print(f'Reached Base Case')
        return A[i:last_digit+1]

    # Divide
    else:
        mid = (i + j) // 2
        j = mid
        print(f"i is {i} and j is {j}")
        print(f'left: {A[i:j]}')
        print(f'right: {A[j:last_digit+1]}')
        breakpoint()

        mergesort(A, i=i, j = j)
        mergesort(A, i = mid, j = last_digit)
	
	# Conquer
        return merge(A, i, j, last_digit)
        
if __name__ == '__main__':

	# A = [34,57,70,19,48,2,94,7,63,75]
	A = [7,8,5,4,3,2,1,9]

	print(mergesort(A))

