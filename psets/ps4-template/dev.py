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

        # Augmentation
        # Manter sempre a soma até aquele elemento da direita
        A.sum = A.item.val

        if A.left:
            A.sum += A.left.sum
            A.max_key = A.item.key

        if A.right:
            A.sum += A.right.sum
            # se estamos pegando somas da direita, a maxima chave passa a ser o da direita
            A.max_key = A.right.item.key

        # Recursive function to call augmentation

class Part_B_Tree(Set_AVL_Tree):
    def __init__(A): 
        super().__init__(Part_B_Node)

    def max_prefix(A):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        s = 0

        # se estou em um node folha, posso retornar que para ele que o key é sua chave e a soma é seu item.val
        if A.left is None and A.right is None:
            # Se nao tenho node, nao tem o que somar
            return (A.item.key, A.item.val)
        
        

        # atualizar o k
        if A.left:
            # descendo na árvore
            (k_left, s_left) = A.left.max_prefix()

            # compara a soma, se incluimos o no pai ou nao, ou mantem soh da esquerda
            s_parent = A.item.val
            sum_s = s_left + s_parent

            if sum_s > s_parent:
                k = A.item.key
                s = sum_s
            else:
                k = k_left

        if A.right:
            (k, s) = A.right.max_prefix()

            # compara a soma do meu atual (s) com incluindo os da direita
            # vamos ver se manter os da esquerda compensa mais que pegar os da direita (neste caso child right nao node parent)
            sum_s = s 





        
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
    B.build(elements)















