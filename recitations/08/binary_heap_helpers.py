# Helper functions to get childs left and right node from parent node i
# and get parent node i from the childs left and right node

def parent(i):

    p = (i - 1) // 2

    return p if i > 0 else i

def left(i, n):
    _left = 2 * i + 1

    # can't return element out of the bounds of the array 
    return _left if _left < n else i

def right(i, n):
    _right = 2 * i + 2
    return _right if _right < n else i

'''
The most important methods will be the max_heapify_up and 
max_heapify_down 
'''

def max_heapify_up(A, n, child):
    # the n which goes increasing from the base class 
    # guarantees we will insert every item in A
    # in fact it will execute the heapify up method as
    # necessary by the condition of the Max Heap Property

    # print(f'\n heapify up')
    # print(A)

    _parent = parent(child)

    # if the parent is less than the child
    if A[_parent].key < A[child].key:
        # print(f'Swap: {A[child]} and {A[_parent]}')
        # breakpoint()
        A[child], A[_parent] = A[_parent], A[child]

        # recurse on
        # parent now will be child 
        # and compare the parent of this parent(child)
        max_heapify_up(A, n, _parent)

def max_heapify_down(A, n, _parent):
    # recursive part with the _parent being next child

    # print(f'\n heapify down')
    # print(A)

    _left, _right = left(_parent, n), right(_parent, n)
    child = _left if A[_left].key > A[_right].key else _right

    if A[child].key > A[_parent].key:
        # print(f'Swap: {A[_parent]} and {A[child]}')
        # breakpoint()
        A[_parent], A[child] = A[child], A[_parent]

        # going down, the before parent, which now is a child 
        # may have childs of its own, and we must check if this new 
        # parent must be swapped with their childs
        max_heapify_down(A, n, child)


def build_max_heap(A):
    '''
    The trick to build in linear time 
    Building from leaves to the root executing the 
    max_heapify_down. 
    This makes that when reaching the leaves, there are no more 
    heapifies to make
    '''

    n = len(A)
    for i in range(n //2, -1, -1):
        max_heapify_down(A, n, i)

    print(A)

    return A