from binarytreejoinsubroutines import BinaryNode

tree = BinaryNode('A')

tree.subtree_insert_before(BinaryNode('B'))
tree.left.subtree_insert_before(BinaryNode('D'))
tree.left.subtree_insert_after(BinaryNode('E'))
tree.left.left.subtree_insert_before(BinaryNode('F'))
tree.subtree_insert_after(BinaryNode('C'))

print('1 - full tree')
print(tree)

print('\nsubtree first')
first = tree.subtree_first()
print(first)

print('\nsubtree last')
last = tree.subtree_last()
print(last)

print('\nPredecessor of tree')
predecessor = tree.predecessor()
print(predecessor)

print('\nSuccessor of tree')
successor = tree.successor()
print(successor)