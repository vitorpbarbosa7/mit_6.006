
class PriorityQueue:
    def __init__(self, A):
        self.n, self.A = 0, A

    def insert(self):
        if not len(self.A) > self.n:
            raise IndexError('insert into full priority queue')
        self.n += 1

    def delete_max(self):
        if self.n < 1:
            raise IndexError('pop from empty priority queue')
        self.n -= 1

    @classmethod
    def sort(Queue, A):
        
        # make empty priority queue
        priorityqueue = Queue(A)
        for _ in range(len(A)):
            # the logic here is to guarantee the insertion will be executed n times
            # the self.n += 1 will increase it 
            priorityqueue.insert()

        for _ in range(len(A)):
             # the self.n -= 1 will decrease the size
             priorityqueue.delete_max()
            
        return priorityqueue.A