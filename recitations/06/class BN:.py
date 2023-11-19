class BN:

    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None

    def st_iter(A):

        if A.left: 
            yield from A.left.st_iter()

        yield A 

        if A.right: 
            yield from A.right.st_iter()

    def __repr__(A):
        return ' -> '.join(str(node.item) for node in A.st_iter())
 
    def st_first(A):

        if A.left: 
            return A.left.st_first()
        else: 
            return A
            
    def st_last(A):

        if A.right:
            return A.right.st_last()
        
        else:
            return A
        
    def successor(A):
        
        if A.right:
            return A.right.st_first()
        
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent


    def predecessor(A):

        if A.left:
            return A.left.st_last()

        while A.parent and(A is A.parent.left):
            A = A.parent
        return A.parent

    def st_insert_before(A, B):

        if A.left:
            A = A.left.st_last()
            A.right = B
            B.parent = A

        else:
            A.left = B
            B.parent = A

    def st_insert_after(A, B):
        
        if A.right:
            A = A.right.st_first()
            A.left = B
            B.parent = A

        else:
            A.right = B
            B.parent = A


    def st_delete(A):

        if A.left or A.right:

            if A.left: 
                B = A.predecessor()

            else:
                B = A.successor()
            
            B.item, A.item = A.item, B.item

            return B.st_delete(A)
        
        
        if A.parent:

            if A.parent.left:
                A.parent.left = None
            else:
                A.parent.right = None
            
            return A

items = [1,2,3,4,5,6]   

def inortraversal(items):

    n = len(items)
    if n < 3:
        left = items[0]
        right = 
    mid = n // 2
    left = items[:mid]
    root_st = items[mid]
    right = items[(mid+1):]
    
    tree = BN(root_st)

    if len(left) > 1:
        left = inortraversal(left)
    elif len(left) == 1:
        left = left[0]
    else:
        left = None
    
    if len(right) > 1:
        right = inortraversal(right)
    elif len(right) == 1:
        right = right[0]
    else: 
        right = None

    if isinstance(left, BN):
        tree.left = left
    else:
        tree.st_insert_before(BN(left))

    if isinstance(right, BN):
        tree.right = right
    else:
        tree.st_insert_after(BN(right))

    return tree


tree = inortraversal(items)



    




