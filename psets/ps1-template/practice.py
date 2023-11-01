from Doubly_Linked_List_Seq import Doubly_Linked_List_Node, Doubly_Linked_List_Seq

# node1 = Doubly_Linked_List_Node(x = 1)
# node2 = Doubly_Linked_List_Node(x = 2)
# node1.next = node2
# node2.prev = node1
# print(node1)

dll = Doubly_Linked_List_Seq()

# X = [1,2,3,5,6,7,8,9,10]

# print(f'Builded')
# dll.build(X)
# print(dll)

# print(f'\nInsert first twice')
# dll.insert_first(99)
# dll.insert_first(99)
# print(dll)

# print(f'\nInsert last twice')
# dll.insert_last(66)
# dll.insert_last(66)
# print(dll)

# print(f'\nDelete first twice')
# dll.delete_first()
# dll.delete_first()
# print(dll)

# print(f'\nDelete last twice')
# dll.delete_last()
# dll.delete_last()
# print(dll)

# print(f'\nRemove algorithm')
# x1 = dll.head.later_node(3)
# x2 = dll.head.later_node(6)

# print(f'Current List: {dll}')

# print(f'Nodes to be removed are {x1} to {x2}')
# L2 = dll.remove(x1, x2)
# print(f'New DoublyLinkedList from removed nodes: {L2}')
# print(f'Remaining List: {dll}')

# # Test remove
# print('# ---------------- #')
# X = [1,2,3,4,5]
# dll = Doubly_Linked_List_Seq()
# dll.build(X)
# print(f'Current List: {dll}')
# x1 = dll.head.later_node(2)
# x2 = dll.head.later_node(4)
# print(f'Nodes to be removed are {x1} to {x2}')
# L2 = dll.remove(x1, x2)
# print(f'New DoublyLinkedList from removed nodes: {L2}')
# print(f'Remaining List: {dll}')


# Test Splice:
X1 = [1,2,3,4,5]
X2 = [6,7,8,9,10]

L1 = Doubly_Linked_List_Seq()
L1.build(X1)
L2 = Doubly_Linked_List_Seq()
L2.build(X2)

print(L1)
print(L2)

node_x = L1.head.later_node(2)
print(f'Node from list L1 to use as x splice point: {node_x}')
print(f'\nSplice result:')
L1.splice(node_x, L2)
print(L1)


