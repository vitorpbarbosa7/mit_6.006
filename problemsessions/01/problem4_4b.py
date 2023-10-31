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
    
    next_node_mid = node_mid.later_node(1)
    _helper_inverse_nodes(node_mid, next_node_mid)

    for item in L:
        print(item)
    # node_mid.next = None
    # node_mid.next = final_node


def _helper_inverse_nodes(node_a:LinkedListNode, node_b):

    print(f'\nStack frame created')
    print(node_a.item)
    print(node_b.item)
    breakpoint()

    if node_a.next is not None and node_b.next is not None:

        next_node = node_b.later_node(1)

        _helper_inverse_nodes(node_b, next_node)

        node_b.next = node_a

    else: 
        return 


reorder_students(L)

# node_mid = L.head.later_node(3)
# print(node_mid.item)

