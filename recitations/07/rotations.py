
'''
All those A, B, C and E new variables, are the necessary variables to execute the rotation of the tree

that is why the AVL Sort algorihtm is not an inplace algorithm as the Heap Sort will be (using tree and array ?)

So we're not using only n slots of memory, we're needing more slots
'''
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
    B.left, B.righ = A, D
    D.left, D.right = C, E

    # if A exists, them A will have B as parent (B will be new root node from this subtree)
    if A: A.parent = B
    # if E exists, it will have the D node as its parent
    if E: E.parent = D

    B.subtree_update()
    D.subtree_update()

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
