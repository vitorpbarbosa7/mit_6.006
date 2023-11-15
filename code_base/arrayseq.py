class ArraySeq:

    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self): self.size
    def __iter__(self): yield from self.A

    def __repr__(self):
        return '['  + ', '.join(str(x) for x in self.A) + ']'
    
    def build(self, X):
        self.A = [a for a in X]     #in python, pretend this builds a static array
        self.size = len(self.A)

    # O(1)
    def get_at(self, i): return self.A[i]

    # O(1)
    # get at the index and set it to the new value
    def set_at(self, i, x): self.A[i] = x

    # O(n)
    # pass it a array A, which will receive the i + k item to the i + k location
    # relation between i and j?
    def _copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j + k] = self.A[i + k]

    # O(n)
    def _copy_backward(self, i, n, A, j):
        for k in range(n-1, -1, -1):
            A[j + k] = self.A[i + k]

    # O(n)
    def insert_at(self, i, x):
        n = len(self.A)

        # ---------------------------------
        # ALLOCATING A WHOLE NEW ARRAY
        # new array will have an extra space
        A = [None] * (n + 1)

        # copy same location
        self._copy_forward(i = 0, n = i, A = A, j = 0)
        A[i] = x

        # copy adding 1 to locations, that is why i + 1
        self._copy_forward(i = i, n = n-2, A = A, j = i+1)

        # now the self receives A rebuilded temporary here
        self.build(A)

    # O(n)
    def delete_at(self, i):
        n = len(self.A)

        # --------------------------------
        # ALLOCATE A NEW ARRAY
        # new array with less space, since we're deleting
        A = [None] * (n-1)

        # copy same location
        self._copy_forward(i = 0, n = i, A = A, j = 0)
        x = self.A[i]

        # copy one lower
        # should't it be copy_backward?
        self._copy_forward(i+1, n - i -1, A, i)
        
        # now the self receives A rebuilded temporary here
        self.build(A)

        # return since it is a delete operation
        return x

    # Since is Static Array, all insertions and delete will take 
    # O(n) time since will be necessary to rebuild the 
    # whole data structure
    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)




if __name__ == '__main__':
    A = [5,3,2,6,4,9]

    arrayseq = ArraySeq()
    arrayseq.build(A)

    print(arrayseq)

    get_at = arrayseq.get_at(3)
    print(get_at)

    # set operation, not insert operation
    arrayseq.set_at(2, 77)
    print(arrayseq)

    # INSERT
    arrayseq.insert_at(2, 99)
    print(arrayseq)

    # DELETE
    deleted = arrayseq.delete_at(5)
    print(deleted)
    print(arrayseq)


    



