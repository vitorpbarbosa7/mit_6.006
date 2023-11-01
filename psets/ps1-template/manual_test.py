from Doubly_Linked_List_Seq import Doubly_Linked_List_Seq

dll = Doubly_Linked_List_Seq()

dll.insert_last(3)
dll.insert_first(2)
dll.insert_last(8)
dll.insert_first(2)
dll.insert_last(9)
dll.insert_first(7)
dll.delete_last()
dll.delete_last()
dll.delete_first()

# ('splice/remove', 1, 2),
# ('splice/remove', 1, 2),
# ('splice/remove', 1, 2),
# ('splice/remove', 1, 2),
# ('splice/remove', 1, 2)