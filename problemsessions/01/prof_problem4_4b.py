from linkedlistseq import LinkedListSeq, LinkedListNode

sequence = ['A','B','C','D','E','F','G','H']

L = LinkedListSeq()
L.build(sequence)

def reorder_students(L):

    n = len(L) // 2

    # get first node
    a = L.head

    # traverse till half position node
    for _ in range(n-1):
        a = a.next

    b = a.next

    # keep track of previous and current node (b)
    x_p,  x = a, b

    for _ in range(n):
        x_n = x.next

        # repoinint the x, to x_previous instead of the current x_n it was
        x.next = x_p

        # get x_p to be current x, and x to be the x_n we will remap in next iteration
        x_p, x = x, x_n

    c = x_p
    a.next = c
    b.next = None

    a = L.head
    for _ in range(n):
        print(a)
        a = a.next
        
    return


reorder_students(L)
