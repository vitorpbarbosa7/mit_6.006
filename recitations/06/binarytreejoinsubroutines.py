from typing import Type, Optional
from elementkey import E

class BinaryNode:

    def __init__(A, x):
        A.item = E(x)
        A.left: Optional[BinaryNode] = None
        A.right: Optional[BinaryNode] = None
        A.parent: Optional[BinaryNode] = None

    def subtree_iter(A):
    # every node in the left subtree of node <x> comes before <x> in the traversal order
    # every node in the right subtree of node <x> comes after <x> in the traversal order

        if A.left: 
            yield from A.left.subtree_iter()

        yield A 

        if A.right: 
            yield from A.right.subtree_iter()

    # def __repr__(A):
    #     return ' -> '.join(str(node.item) for node in A.subtree_iter())

    def __repr__(A):
        return str(A.item)
 
    def subtree_first(A):
        '''Traversing left, as in the traversal order, left comes first'''

        if A.left: 
            return A.left.subtree_first()
        else: 
            return A
            
    def subtree_last(A):
        '''Traversing right, as in the traversal order, right comes after'''

        if A.right:
            return A.right.subtree_last()
        
        else:
            return A
        

    # Successor - Predecessor 

    def successor(A):
        
        # if it has a right subtree, the successor will be the left most node in the right subtree
        # so we go right once, and left as much as possible after
        # for that we can use the created method for in any tree go subtree_first()
        if A.right:
            return A.right.subtree_first()
        
        # while the parent of A exists and 
        # if it was left of parent, then the parent is the successor, that's why put the condition 
            # A.parent.right, because if it is right, must continue going up, until the node we reach is left node of parent and not right node of parent
            # that is why we return the A.parent in which we're
            # see that we update the A at each step, going up in the tree
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent


    def predecessor(A):
        
        # if left exists, we consider so the left node as root, and from this root, the subtree defined, we will traverse it until find the right most node
        # this right most node can be found by using the subtree_last subroutine
        if A.left:
            return A.left.subtree_last()
        
        # A.parent.right would satisfy our condition in the case that A has no left node
        # The predecessor will be found by going up in the tree, and if it is the right child of parent, that parent is the predecessor
        
        # if not, we must continue going up until the parent has the A as right child, so the parent will the predecessor 
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):
        '''
        Insert node <B> before node <A>
        '''
        # if A has a left node, not the easy case
        # we must insert the B at the right most node from the left subtree
        # we can get to the right most node of the left subtree of A using the subtree_last() subroutine, that is, always going right
        if A.left:
            A = A.left.subtree_last()
            A.right = B
            B.parent = A

        else:
            A.left = B
            B.parent = A

    def subtree_insert_after(A, B):
        '''
        Insert node <B> after node <A>
        '''
        # if it has a right node
        # then we must insert it after the left most node of the right subtree
        if A.right:
            A = A.right.subtree_first()
            A.left = B
            B.parent = A

        else:
            A.right = B
            B.parent = A


    def subtree_delete(A):

        # if it not a leaf, we're not at the easy trivial case
        # 
        if A.left or A.right:

            # if has a left child, we go to find the precessor of A, by using the predecessor subroutine
            # with that predecessor, we swap him with the desired item A to be deleted
            if A.left: 
                B = A.predecessor()

            # if it has no left child, but the right child, we go to the successor of A in the right subtree
            else:
                B = A.successor()
            
            B.item, A.item = A.item, B.item

            # now our B is the item we want to delete, so call the function again to continue swaping until becomes a leaf
            return B.subtree_delete()
        
        # if did entered the first case, and has a parent, it is a leaf
        if A.parent:

            # check if A is left child of parent, if it is deleting is setting the A.parent.left = None
            if A.parent.left is A:
                A.parent.left = None

            # else it was the right node, so set the parent here to None
            else:
                A.parent.right = None
            
            return A
        

# Example usage
if __name__ == '__main__':
    tree = BinaryNode('A')

    tree.subtree_insert_before(BinaryNode('B'))
    tree.left.subtree_insert_before(BinaryNode('D'))
    tree.left.subtree_insert_after(BinaryNode('E'))
    tree.left.left.subtree_insert_before(BinaryNode('F'))
    tree.subtree_insert_after(BinaryNode('C'))

    print('1 - full tree')
    print(tree)

    print('\nsubtree first')
    first = tree.subtree_first()
    print(first)

    print('\nsubtree last')
    last = tree.subtree_last()
    print(last)

    print('\nPredecessor of tree')
    predecessor = tree.predecessor()
    print(predecessor)

    print('\nSuccessor of tree')
    successor = tree.successor()
    print(successor)

    print(f'\nDelete node {tree.left.left.item}')
    deleted = tree.left.left.subtree_delete()
    print(deleted)








