from binarynode_avl import BinaryNode

class SizeNode(BinaryNode):

    '''Need to implement a node which has a size as a augmentated property'''
    
    def subtree_update(A):
        super().subtree_update()

        # each single node counts as 1 in size
        A.size = 1

        # if it has left and right nodes, so the size will be incremented by each of nodes in left and right subtrees 
        # as a recursion, when gets to the last node (leaf) this leaf will count as 1
        if A.left:
            A.size += A.left.size
        if A.right:
            A.size += A.right.size

    def subtree_at(A, i):
        '''Method to traverse the tree as a sequence (which contains items which have extrinsic order)'''
    
        assert i >= 0 # at least one node

        if A.left:
             L_size = A.left.size # this left node will (like a recursion, but O(1)) have a size accounted for the subtree
        else: 
             L_size = 0
    	
        # with this condition we go left or right
        if i < L_size:
    		# recursively go left first and decide what to do after with the next subtree with the recursion
            return A.left.subtree_at(i)
    	# go right
        elif i > L_size:
            return A.right.subtree_at(i - L_size - 1)
        
        else:
            return A
		
# Example Usage
if __name__ == '__main__':

    tree = SizeNode('A')

    tree.subtree_insert_before(SizeNode('B'))
    tree.subtree_insert_before(SizeNode('C'))
    tree.subtree_insert_before(SizeNode('D'))
    tree.subtree_insert_before(SizeNode('E'))
    tree.subtree_insert_before(SizeNode('F'))
    tree.subtree_insert_before(SizeNode('F'))
    tree.subtree_insert_before(SizeNode('F'))
    tree.subtree_insert_before(SizeNode('G'))
    tree.subtree_insert_before(SizeNode('G'))

    # don't care about the order, the h must be logn 
    print(tree.height)
    print(tree.size)
    print(tree.min)


    elements = [tree.subtree_at(x) for x in range(tree.size)]
    print(elements)

    