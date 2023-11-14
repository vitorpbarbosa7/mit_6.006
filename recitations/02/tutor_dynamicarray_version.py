class DynamicArraySeq:

    def __init__(self, r=2):
        self.A = []
        self.size = 0
        self.r = r
        self.upper, self.lower = len(self.A), len(self.A) // (self.r * self.r)
        self._resize(0)

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(len(self)):
            yield self.A[i]

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def _compute_bounds(self):
        self.upper, self.lower = len(self.A), len(self.A) // (self.r * self.r)

    def _resize(self, n):
        if self.lower < n < self.upper:
            return
        m = max(n, 1) * self.r
        A = [None] * m
        A[:self.size] = self.A[:self.size]
        self.A = A
        self._compute_bounds()

    def insert_last(self, x):
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i, x):
        self.insert_last(None)
        self.A[i + 1:self.size + 1] = self.A[i:self.size]
        self.A[i] = x

    def delete_at(self, i):
        x = self.A[i]
        self.A[i:self.size - 1] = self.A[i + 1:self.size]
        self.delete_last()
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)


if __name__ == '__main__':
    A = [5, 3, 2, 6, 4, 9]
    dynamicarray = DynamicArraySeq()
    dynamicarray.build(A)
