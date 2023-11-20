def _height(A):
    '''Omega(n)-time algorithm to recursively compute the height, considering the subtrees
    This is not our desire, we want to compute this in constant time O(1) using data structure augmentation'''

    # default -1 height for a None node (after a leaf)
    # height of leaf will be 0 , right?
    if A is None: return -1 
    return 1 + max(height(A.left), A.right)

def height(A):
    # height being a property (augmentation)
    if A: return A.height
    else: return -1

    def subtree_update(A):
        A.height = 1 + max(height(A.left), height(A.right))



def subtree_update(A):
    pass

def skew(A):
    '''Gets the skew of a node'''
    return height(A.right) - height(A.left)
    
def rebalance(A):
    if A.skew() == 2:
        if A.right.skew() < 0:

            # rotate right on A.right
            A.right.subtree_rotate_right()
        
        # after fixed the right part, do the default rotate_left for this case
        A.subtree_rotate_left()

    elif A.skew() == -2:
        if A.left.skew() > 0:
            A.left.subtree_rotate_left()

        # after fixed left side, do the default rotate_right step for this case
        A.subtree_rotate_right()


def maintain(A):
    A.rebalance()
    A.subtree_update()
    
    # go up in the tree recursively maintaining invariants
    if A.parent: A.parent.maintain()

