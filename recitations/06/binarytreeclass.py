from binarytreejoinsubroutines import BinaryNode

class BinaryTree:
    def __init__(T, NodeType = BinaryNode):
        T.root = None
        T.size = 0
        T.NodeType = NodeType

    def __len__(T):
        return T.size 
        # return len([x for x in btree]) ??

    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item

# Example usage:
if __name__ == '__main__':
    tree = BinaryNode('A')

    tree.subtree_insert_before(BinaryNode('B'))
    tree.left.subtree_insert_before(BinaryNode('D'))
    tree.left.subtree_insert_after(BinaryNode('E'))
    tree.left.left.subtree_insert_before(BinaryNode('F'))
    tree.subtree_insert_after(BinaryNode('C'))

    btree = BinaryTree()
    btree.root = tree
    print(btree.root)
