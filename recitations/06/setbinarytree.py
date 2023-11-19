from binarytreeclass import BinaryTree
from bstnode import BSTNode

class SetBinaryTree(BSTNode):

    def __init__(self):
        super().__init__(BSTNode)

    def iter_order(self):
        yield from self

    def build(self, X):
        for x in X: self.subtree_insert(x)

    def find_min(self):
        if self.root: return self.root.subtree_first().item

    def find_max(self):
        if self.root: return self.root.subtree_last().item

    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node:
                return node.item
            
    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node:
                return node.item
            
    def find_prev(self, k):
        if self.root:
            node = node.root.subtree_find_prev()
            if node:
                return node.item
            
    def insert(self, x):
        new_node = self.NodeType(x)
        if self.root:
            self.root.subtree_insert(new_node)

            # ???
            if new_node.parent is None:
                return False
            
            # if the new node has no parent node, it is the root
            # set the root of the tree to the new node
            else:
                self.root = new_node
            self.size += 1
            return True
        
    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()

        # if the deleted node was the parent node (node.parent == None)
        # it was the deleted node, if it was the deleted
        # so the new root of the tree must be set to None, be satisfy
        # the invariant of root node not having parent node
        if ext.parent is None:
            self.root = None

        self.size -= 1
        return ext.item
    
class E:
    def __init__(self, key):
        self.key = key

# Example Usage
elements = ['F','D','B','E','A','C']

items = [BSTNode(E(el)) for el in elements]
print(items)

setbinarytree = SetBinaryTree()
setbinarytree.build(items)
print(setbinarytree)

