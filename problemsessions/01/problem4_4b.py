from linkedlistseq import LinkedListSeq, LinkedListNode

sequence = ['A','B','C','D','E','F','G','H']

L = LinkedListSeq()
L.build(sequence)

def reorder_students(L:LinkedListSeq):

    mid = len(L)//2
        
    node_mid = L.head.later_node(mid)
    print(node_mid.item)
    print('passou aqui')

    # breakpoint()
    
    final_node = _helper_inverse_nodes(node_mid)
    node_mid.next = None
    node_mid.next = final_node


def _helper_inverse_nodes(node:LinkedListNode):

    print(f'\nStack frame created')
    print(node.item)
    breakpoint()

    if node.next is not None:
        
        # next node
        next2_node = node.later_node(2)
        next_node = node.later_node(1)
        
        # next node points to previous node
        next2_node.next = next_node
        
        _helper_inverse_nodes(next_node)

    # reached final node
    if node.next == None:
        return node


reorder_students(L)

# node_mid = L.head.later_node(3)
# print(node_mid.item)

