from Doubly_Linked_List_Seq import Doubly_Linked_List_Node, Doubly_Linked_List_Seq

# node1 = Doubly_Linked_List_Node(x = 1)
# node2 = Doubly_Linked_List_Node(x = 2)
# node1.next = node2
# node2.prev = node1
# print(node1)

dll = Doubly_Linked_List_Seq()

X = [1,2,3]

dll.build(X)

dll.insert_first(9)

print(dll)