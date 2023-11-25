def height(A):
    if A:
         return A.height
    else:
        return -1
        
class BinaryNode:
    # O(1) - initialize takes constant time
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None

        # subtree update will be responsible for getting our beautiful augmentatio property
        # in this case, using only height
        A.subtree_update()

    def __repr__(A):
        return str(A.item)

    # def __str__(A):
    #     return str(A.item)

    # O(1) - with augmentation height
    def subtree_update(A):
        '''
        A.height
        A.subtree_ones (can be subtree sum of items if not only storing 0 and 1s)
        '''

        # in this subtree augmentations properties, the recursion and the augmentation itself is allowed by
        # calling the left and right subtrees
        # think about applying from bottom up in the tree 

        # Every time we do something, update the augmentation properties
        A.height = 1 + max(height(A.left), height(A.right))

        # another property for subtree augmentation
        A.subtree_ones = A.item

        if A.left:
            A.subtree_ones += A.left.subtree_ones

        if A.right:
            A.subtree_ones += A.right.subtree_ones

    # O(1) - if height is a property, them this will run in constant time 
    def skew(A):
        return height(A.right) - height(A.left)

    # O(n) - traverse all items will take linear time anyway
    def subtree_iter(A):
        if A.left:
            yield from A.left.subtree_iter()
        
        yield A 

        if A.right:
            yield from A.right.subtree_iter()

    # O(logn) - get first element of a subtree will take logn time because we benefit from binary search structure
    def subtree_first(A):
        if A.left: 
            return A.left.subtree_first()
        else:
            return A

    # O(logn) same logic as subtree_first()
    def subtree_last(A):
        if A.right:
            return A.right.subtree_last()
        else:
            return A
    
    # O(logn) - might go down or up logn
    def successor(A):
        if A.right:
            return A.right.subtree_first()

        # go up in the tree
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    # O(logn) - same logic as successor (symmetric)
    def predecessor(A):
        if A.left:
            return A.left.subtree_last()

        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    # O(logn) Same logic as successor and predecessor, and subtree_first and last, traversing takes O(logn)-time
    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A

        A.maintain()

    # O(logn) - same logic as subtree_insert_before
    def subtree_insert_after(A, B):

        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A

        A.maintain()

    # O(logn) - as we expected, all operations are taking logn time to be executed, even dynamic ones
    def subtree_delete(A):
        if A.left or A.right:
            if A.left:
                B = A.predecessor()
            else:
                B = A.sucessor()

            A.item, B.item = B.item, A.item
            
            # make the swaps recursively until gets to a leaf
            return B.subtree_delete()

        if A.parent:
            if A.parent.left is A:
                # deletion operation
                A.parent.left = None
            else:
                A.parent.right = None
        
        # return the deleted node object
        return A

    # O(1) : rotation takes constant time 
    def subtree_rotate_right(D):
        # wether there is no a left of D 
        # D left must exist in order to rotate right the D and make the B (D.left) go up
        assert D.left

        # get the local names
        # B and E will be the left and right nodes of reference D (which will be rotated right)
        B, E = D.left, D.right
        # A and C will be B left and right
        A, C = B.left, B.right

        # swap D and B nodes 
        # this way, I will not need to set the B.parent to None, because the D alread have it 
        # the thing here is that the pointes of D and B will be swaped and we will have to only take the intrinsec item of each one back 
        D, B = B, D
        # the new D must take back his item 
        # the new B must take back his item
        D.item, B.item = B.item, D.item

        # following the picture, the B now will have the left and right nodes as A and D 
        # D will have left and right node as C and E 
        B.left, B.right = A, D
        D.left, D.right = C, E

        # if A exists, them A will have B as parent (B will be new root node from this subtree)
        if A: A.parent = B
        # if E exists, it will have the D node as its parent
        if E: E.parent = D

        # B and D changed their relative position in the overall tree considering children
        # So B and D must be updated their agumented properties
        B.subtree_update()
        D.subtree_update()

    # O(1) : rotation takes constant time     
    def subtree_rotate_left(B):
        assert B.right

        A, D = B.left, B.right
        C, E = D.left, D.right

        B, D = D, B
        B.item, D.item = D.item, B.item

        D.left, D.right = B, E
        B.left, B.right = A, C

        if A: A.parent = B
        if E: E.parent = D

        B.subtree_update()
        D.subtree_update()





    # update all ancestors 
    # O(logn)
    def maintain(A):
        A.rebalance()
        
        # update the heights
        A.subtree_update()
        # go up maintaining the invariants of the binary tree
        if A.parent: A.parent.maintain()

    # O(1)
    def rebalance(A):
        if A.skew() == 2:
            if A.right.skew() < 0:
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew() == -2:
            if A.left.skew() > 0 :
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()

# Example usage
if __name__ == '__main__':

    tree = BinaryNode('A')

    # force a completely craze linar unbalaced tree and the avl structure must make the updates necessaries for
    # the invariants to be kept and everything continue to run in O(logn)
    tree.subtree_insert_before(BinaryNode('B'))
    tree.subtree_insert_before(BinaryNode('D'))
    tree.subtree_insert_before(BinaryNode('E'))
    tree.subtree_insert_after(BinaryNode('F'))
    tree.subtree_insert_after(BinaryNode('C'))
 
    print(tree)