from binarytreejoinsubroutines import BinaryNode

class BSTNode(BinaryNode):

    def subtree_find(A, k):
        '''Binary search of key'''
        
        # if k less them first item (rootsubtree)
        if k < A.item.key:
            # if left still exists continue trying to find in the subtree
            if A.left:
                return A.left.subtree_find(k)
            
        # right subtree
        elif k > A.item.key:
            if A.right:
                return A.right.subtree_find(k)
        else:
            return A
        
        return None
    
    def subtree_find_next(A, k):
        if k >= A.item.key:
            if A.right: 
                return A.right.subtree_find_next(k)
            else: 
                return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            # if B not None
            if B:
                return B
            
        # else the root will be returned
        return A
    
    def subtree_find_prev(A, k):
        if k <= A.item.key:
            if A.left: 
                return A.left.subtree_find_prev(k)
            else: 
                return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B:
                return B
        return A
    
    def subtree_insert(A, B:BinaryNode):
        '''Method responsible for inserting items in 
        the set interface, in key order, therefore it uses the logic 
        of binary search, that's why when buildint the set interface using 
        the data structure binary tree, it will take O(nlogn)'''

        # left case insert befores
        if B.item.key < A.item.key:
            if A.left:
                A.left.subtree_insert(B)
            else:
                A.subtree_insert_before(B)

        # right case insert after
        elif B.item.key > A.item.key:
            if A.right:
                A.right.subtree_insert(B)
            else:
                A.subtree_insert_after(B)

        # if the keys are equal
        # set the same key, maybe putting the same key with different values?
        # the item itself has a key and value
        else:
            A.item = B.item




                



        
