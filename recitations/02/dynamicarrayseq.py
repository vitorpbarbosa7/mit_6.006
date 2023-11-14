from arrayseq import ArraySeq

class DynamicArraySeq(ArraySeq):

    def __init__(self, r = 2):

        # initialize from ArraySeq
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    # O(1) :  size already calculated, dunder len from this object constant time
    def __len__(self):
        return self.size 
    
    # O(n) : as always traversing takes O(n)
    def __iter__(self):
        for i in range(len(self)): yield self.A[i]

    def build(self, X):
        for a in X: self.insert_last(a)

    def _compute_bounds(self):
        ''''Get the maximum size and lower bound for resizing'''
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _resize(self, n):
        # if already within the bounds, do nothing
        if (self.lower < n < self.upper): return 
        
        # maximum new size
        m = max(n, 1) * self.r

        # ----------------------
        # IF REALLY NECESSARY TO RESIZE, ALLOCATE NEW ARRAY
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A

        # keep track of new bounds
        self._compute_bounds()


    def insert_last(self, x):
        # if necessary to resize, do it
        # if not only it will return None from the self._resize and
        self._resize(self.size + 1)
        # it sill finally put it here:
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):
        # just make it to None
        self.A[self.size - 1] = None
        # decrease in size
        self.size -= 1
        # if necessary, resize
        self._resize(self.size)

    def insert_at(self, i, x):
        # create a necessary space in the end if necessary
        self.insert_last(None)
        # go copying each one of them 
        self._copy_backward(i, self.size - (i+1), self.A, i + 1)

        # with empty space left, set it to new value
        self.A[i] = x

    def delete_at(self, i):
        # get the element
        x = self.A[i]
        # element will be overwriten ?
        self._copy_forward(i + 1, self.size  - (i+1), self.A, i)
        # the last None can be deleted
        self.delete_last()

        return x        

    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)


if __name__ == '__main__':
    A = [5,3,2,6,4,9]

    dynamicarray = DynamicArraySeq()
    dynamicarray.build(A)
    print(dynamicarray)

    # Support same operations as Base Class
    get_at = dynamicarray.get_at(3)
    print(get_at)

    # set operation, not insert operation
    dynamicarray.set_at(2, 77)
    print(dynamicarray)

    # INSERT
    dynamicarray.insert_at(2, 99)
    print(dynamicarray)

    # DELETE
    deleted = dynamicarray.delete_at(4)
    print(deleted)
    print(dynamicarray)