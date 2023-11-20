from binarytreeclass import BinaryTree
from sizenode import SizeNode

class SeqBinaryTree(BinaryTree):
    def __init__(self):
        super().__init__(SizeNode)

    def build(self, X):

        # X is kept intact, working with the i and j pointes to move along
        def build_subtree(X, i, j):
            # within a subtree, i and j helps to keep track of what are the lower and upper bounds of that subtree

            c = (i + j) // 2

            root = self.NodeType(X[c])
            
            # must put the element in the left part or current root
            if i < c:
                # imagine entering the first stack after the first one, then the i (which start with 0) is still 0
                # but the 
                root.left = build_subtree(X, i, c-1)
                root.left.parent = root
            
            if c < j:
                root.right = build_subtree(X, c + 1, j)
                root.right.parent = root

            root.subtree_update()

            return root

        self.root = build_subtree(X, 0, len(X) - 1)
        # size of the tree is equal to the size of root
        self.size = self.root.size	

    def get_at(self, i):
        assert self.root

        # using the method from the SizeNode class which traverses using binary search on sizes
        return self.root.subtree_at(i).item
    
    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).item = x
        
    def insert_at(self, i, x):
        new_node = self.NodeType(x)
        # if we want to insert at first, position, obviously it will have to traverse to left most node and insert before
        if i == 0:
            # if the root exists 
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            # if root does not exist, easy case, define the root as this new_node
            else: 
                self.root = new_node
        else:
            # if not the first item, we must search for a reference item before, to insert the desired new value after 
            node = self.root.subtree_at(i-1)
            node.subtree_insert_after(new_node)

        self.size += 1


    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete()
        # if the deleted item has no parent node, it was the root
        if ext.parent is None:
            self.root = None
        self.size -= 1

        return ext.item

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)
        

if __name__ == '__main__':

    X = ['A','B','C','D','E','F','G']

    tree = SeqBinaryTree()
    tree.build(X)
    print(tree)

    zero = tree.get_at(0)
    one = tree.get_at(1)
    print(zero)
    print(one)

    five = tree.get_at(5)
    six = tree.get_at(6)
    print(five)
    print(six)

    print(tree)

    print('\ninsert at')
    tree.insert_at(2, 'H')
    print(tree)
    tree.set_at(1, 'I')
    print(tree)

    print('\ndeleting items')
    deleted = tree.delete_at(3)
    print(deleted)
    print(tree)