def subtree_iter(self):
    # every node in the left subtree of node <x> comes before <x> in the traversal order
    # every node in the right subtree of node <x> comes after <x> in the traversal order


    if self.left: 
        yield from self.left.subtree_iter()

    yield self 

    if self.right: 
        yield from self.right.subtree_iter()



def subtree_first(self):
    '''Traversing left, as in the traversal order, left comes first'''

    if self.left: 
        return self.left.subtree_first()
    else: 
        return self
    
def subtree_last(self):
    '''Traversing right, as in the traversal order, right comes after'''

    if self.right:
        return self.right.subtree_last()
    
    else:
        return self
    


# Successor - Predecessor 

def successor(self):
    
    # if it has a right subtree, the successor will be the left most node in the right subtree
    # so we go right once, and left as much as possible after
    # for that we can use the created method for in any tree go subtree_first()
    if self.right:
        return self.right.subtree_first()
    
    # while the parent of self exists and 
    # if it was left of parent, then the parent is the successor, that's why put the condition 
        # self.parent.right, because if it is right, must continue going up, until where we are is left node of parent, and that parent will be the successor
        # that is why we return the self.parent in which we're
        # see that we update the self at each step, going up in the tree
    while self.parent and (self is self.parent.right):
        self = self.parent
    return self.parent


def predecessor(self):
    
    # if left exists, we consider so the left node as root, and from this root, the subtree defined, we will traverse it until find the right most node
    # this right most node can be found by using the subtree_last subroutine
    if self.left:
        return self.left.subtree_last()
    
    # self.parent.right would satisfy our condition in the case that self has no left node
    # The predecessor will be found by going up in the tree, and if it is the right child of parent, that parent is the predecessor
    
    # if not, we must continue going up until the parent has the self as right child, so the parent will the predecessor 
    while self.parent and(self is self.parent.left):
        self = self.parent
    return self.parent


