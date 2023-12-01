from Set_AVL_Tree import BST_Node, Set_AVL_Tree

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()

        # Augmentations
        A.sum = A.item.val

        # Left and right subtree summation values
        if A.left:
            A.sum += A.left.sum
        
        if A.right:
            A.sum += A.right.sum

        # Max prefix augmentations based on subtree augmentation of sum of values
         
        left = -float('inf')
        right = -float('inf')

        middle = A.item.val

        # if there is a left node, calculate the left subtree prefix (left)
        # also consider a subtree considering current node (middle)
        if A.left:

            # max_prefix left is kept separated, maybe we will use only him
            left = A.left.max_prefix

            # computes middle plus the ones in the left, even without the left prefix
            middle += A.left.sum

        # and let's consider a right subtree
        if A.right:

            # the middle alreay receive all the values from the left
            # we add to it not the sum in the right, but until max_prefix
            # Blackboard day 01/12/2023
            right = middle + A.right.max_prefix

        # We will get the max prefix by comparing if the left, middle or right subtree are the greatest or not
        # thinking about the most a most left node which is not leaf, still parent, and has left child and right child
        # # it will calculate, for that subtree what is the combination, if with left only, if with left and middle (parent),
        # or with left, middle and right nodes, and will store the max value
        # That maximum value will propagate for higher values 

        # leaf nodes will fall directly here, so left and right could not be 0, since 
        # the negative values are allowed in this problem
        A.max_prefix = max(left, middle, right)

        # Max prefix key augmentation
        if left == A.max_prefix:
            A.max_prefix_key = A.left.max_prefix_key
        
        elif middle == A.max_prefix:
            A.max_prefix_key = A.item.key
        
        else:
            A.max_prefix_key = A.right.max_prefix_key

        # At each inserted node makes the necessary rotations and update the 
        # Augmentations within the tree for all individual nodes 
        # print(A)
        # breakpoint()

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0

        k = self.root.max_prefix_key
        s = self.root.max_prefix

        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0

    # sort by one of the keys, this list of tuples
    toppings.sort(key = lambda topping: topping[0])

    for (x, y, t) in toppings:
        B.insert(Key_Val_Item(y,t))
        
        (YY, TT) = B.max_prefix()

        if T < TT:
            X, Y, T = x, YY, TT
    
    return (X, Y, T)


if __name__ == '__main__':
    # toppings = [(-7, 8, 5), (2, -4, 3), (7, 10, -1), (4, -3, 9), (-5, 1, 9)]
    toppings = [(8,8,-7), (-6,-3,2), (1,-1,6), (9,9,12),(12, 12, -13)]

    result = tastiest_slice(toppings)

    print(result)


