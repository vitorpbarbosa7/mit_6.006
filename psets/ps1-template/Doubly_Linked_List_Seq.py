class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)
    
    def __repr__(self):
        return f'{self.item}    '

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        pass

    def insert_last(self, x):
        
        new_node = Doubly_Linked_List_Node(x)

        # Base Case, empty DoublyLinkedList
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # Inductive Step, if DoublyLinkedList is not empty
        else:
            current_last_node = self.tail
            self.tail = new_node
            current_last_node.next = new_node
            new_node.prev = current_last_node
            

        

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        pass
