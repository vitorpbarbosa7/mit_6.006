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

    def cv(A):

        for node in A.subtree_iter():
            print(node.item)
            
            predecessor = node.predecessor()
            
            if predecessor:
                add = predecessor.sum
                node.sum += add
                
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















