class Bnode:

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



tree = Bnode('A')

tree.subtree_insert_before(Bnode('F'))
tree.subtree_insert_before(Bnode('D'))
tree.subtree_insert_before(Bnode('B'))
tree.subtree_insert_before(Bnode('E'))
tree.subtree_insert_after(Bnode('C'))

first = tree.subtree_first()




