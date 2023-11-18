def subtree_insert_before(self, B):
    '''
    Insert node <B> before node <self>
    '''
    # if self has a left node, not the easy case
    # we must insert the B at the right most node from the left subtree
    # we can get to the right most node of the left subtree of self using the subtree_last() subroutine, that is, always going right
    if self.left:
        self = self.left.subtree_last()
        self.right = B
        B.parent = self

    else:
        self.left = B
        B.parent = self

def subtree_insert_after(self, B):
    '''
    Insert node <B> after node <self>
    '''
    # if it has a right node
    # then we must insert it after the left most node of the right subtree
    if self.right:
        self = self.right.subtree_first()
        self.left = B
        B.parent = self

    else:
        self.right = B
        B.parent = self


def subtree_delete(self):

    # if it not a leaft, we're not at the easy trivial case
    # 
    if self.left or self.right:

        # if has a left child, we go to find the precessor of self, by using the predecessor subroutine
        # with that predecessor, we swap him with the desired item self to be deleted
        if self.left: 
            B = self.predecessor()

        # if it has no left child, but the right child, we go to the successor of self in the right subtree
        else:
            B = self.successor()
        
        B.item, self.item = self.item, B.item

            # now our B is the item we want to delete, so call the function again to continue swaping until becomes a leaf
        return B.subtree_delete(self)
    
    # if did entered the first case, and has a parent, it is a leaf
    if self.parent:

        # just check if either is left or right child (--politics--)
        if self.parent.left:
            self.parent.left = None
        else:
            self.parent.right = None
        
        return self






