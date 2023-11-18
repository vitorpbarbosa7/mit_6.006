from binarytreejoinsubroutines import BinaryNode

tree = BinaryNode('A')
print(tree.item)

tree.subtree_insert_before(BinaryNode('F'))
tree.subtree_insert_before(BinaryNode('D'))
tree.subtree_insert_before(BinaryNode('B'))
tree.subtree_insert_before(BinaryNode('E'))
tree.subtree_insert_after(BinaryNode('C'))

print(tree)
print(tree.item)