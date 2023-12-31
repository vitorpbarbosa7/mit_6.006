class Binary_Node:
    def __init__(A, x): # O(1)
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update() # wait for R07!

    def subtree_iter(A): # O(n)
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()

    def subtree_first(A): # O(h)
        if A.left: return A.left.subtree_first()
        else: return A

    def subtree_last(A): # O(h)
        if A.right: return A.right.subtree_last()
        else: return A

    def successor(A): # O(h)
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A): # O(h)
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

def subtree_insert_before(A, B): # O(h)
    if A.left:
        A = A.left.subtree_last()
        A.right, B.parent = B, A
    else:
        A.left, B.parent = B, A
        # A.maintain() # wait for R07!

def subtree_insert_after(A, B): # O(h)
    if A.right:
        A = A.right.subtree_first()
        A.left, B.parent = B, A
    else:
        A.right, B.parent = B, A
        # A.maintain() # wait for R07!

def subtree_delete(A): # O(h)
    if A.left or A.right:
        if A.left: B = A.predecessor()
        else: B = A.successor()
        A.item, B.item = B.item, A.item
        return B.subtree_delete()
    if A.parent:
        if A.parent.left is A: A.parent.left = None
        else: A.parent.right = None
    #