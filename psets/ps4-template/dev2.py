from Set_AVL_Tree import BST_Node, Set_AVL_Tree

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)
    
    def __repr__(self):
        return self.__str__()

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()

        # Augmentation
        # Manter sempre a soma até aquele elemento da direita
        # Uma vez com esta soma possso subtrair depois os da direita de cada node?
        # A.sum = A.item.val

        A.sum = A.item.val

        if A.left:
            A.sum += A.left.sum

        if A.right:
            A.sum += A.right.sum

    def prefix_run(A):
        print('\nStack called')
        print(A.item)

        if A.left:
            A.left.prefix_run()        

        if A.right:
            A.right.prefix_run()

        # Leaf nodes:
        if A.left is None and A.right is None:
            if A.parent:

                # if left child node:
                if A.parent.left is A:
                    A.prefix = A.sum

                # if right child node:
                if A.parent.right is A:
                    A.prefix = A.item.val + A.parent.sum

        # if it has left and right nodes and is right child of parent
        if A.left and A.right and A.parent and A.parent.right is A:
            A.prefix = A.sum - A.right.sum + A.parent.sum

        # if it has left and right nodes and is left child of parent
        if A.left and A.right and A.parent and A.parent.left is A:
            A.prefix = A.sum - A.right.sum

        if not A.left and A.right:
            A.prefix = A.item.val

        if not A.right and A.left:

            # if is right child
            if A.parent.right is A:
                A.prefix = A.sum + A.parent.prefix

            if A.parent.left is A:
                A.prefix = A.sum



        # if it is root:
        if A.left and A.right and A.parent is None:
            A.prefix = A.sum - A.right.sum


                
class Part_B_Tree(Set_AVL_Tree):
    def __init__(A): 
        super().__init__(Part_B_Node)

    def max_prefix(A):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0



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

    # construct the elements as keys and values using the class provided
    

    B.build()


    
    return (X, Y, T)

if __name__ == '__main__':

    X = [(-7,5),(2,3),(7,-1),(4,9),(-5,9)] 
    elements = [Key_Val_Item(key, val) for key,val in X]

    B = Part_B_Tree()

    for element in elements:
        B.insert(element)

    B.root.prefix_run()

    print('----------main-------------')
    # print(B.root.prefix)
















