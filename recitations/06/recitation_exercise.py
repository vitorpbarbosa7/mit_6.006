class BNode:

    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None

    def subtree_iter(A):

        if A.left: 
            yield from A.left.subtree_iter()

        yield A 

        if A.right: 
            yield from A.right.subtree_iter()

    def __repr__(A):
        return ' -> '.join(str(node.item) for node in A.subtree_iter())
 
    def subtree_first(A):
        '''Traversing left, as in the traversal order, left comes first'''

        if A.left: 
            return A.left.subtree_first()
        else: 
            return A
            
    def subtree_last(A):

        if A.right:
            return A.right.subtree_last()
        
        else:
            return A
        
    def successor(A):
        
        if A.right:
            return A.right.subtree_first()
        
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent


    def predecessor(A):

        if A.left:
            return A.left.subtree_last()

        while A.parent and(A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):

        if A.left:
            A = A.left.subtree_last()
            A.right = B
            B.parent = A

        else:
            A.left = B
            B.parent = A

    def subtree_insert_after(A, B):
        
        if A.right:
            A = A.right.subtree_first()
            A.left = B
            B.parent = A

        else:
            A.right = B
            B.parent = A


    def subtree_delete(A):

        if A.left or A.right:

            if A.left: 
                B = A.predecessor()

            else:
                B = A.successor()
            
            B.item, A.item = A.item, B.item

            return B.subtree_delete(A)
        
        
        if A.parent:

            if A.parent.left:
                A.parent.left = None
            else:
                A.parent.right = None
            
            return A


items = [1,2,3,4,5,6]
# items = [1,2,3]

def insert_inordertraversal(items):

    n = len(items)
    mid = n // 2

    # Divide
    left = items[:mid]
    root_subtree = items[mid]
    right = items[(mid+1):]
    
    tree = BNode(root_subtree)

    if len(left) > 1:
        left = insert_inordertraversal(left)
    elif len(left) == 1:
        left = left[0]
    else:
        left = None
    
    if len(right) > 1:
        right = insert_inordertraversal(right)
    elif len(right) == 1:
        right = right[0]
    else: 
        right = None

    if isinstance(left, BNode):
        tree.left = left
    else:
        tree.subtree_insert_before(BNode(left))

    # Conquer
    if isinstance(right, BNode):
        tree.right = right
    else:
        tree.subtree_insert_after(BNode(right))

    return tree


tree = insert_inordertraversal(items)



    




