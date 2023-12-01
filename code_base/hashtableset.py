from setinterface import SetFromSeq
from linkedlistseqchainhash import LinkedListSeqChainHash
from random import randint

class HashTableSet:
    def __init__(self, r = 200):
        self.chain_set = SetFromSeq(LinkedListSeqChainHash)
        self.A = []
        self.size = 0
        self.r = r
        self.p = 2**31 - 1
        self.a = randint(1, self.p, 1)
        self._compute_bounds()
        self._resize(0)

    # O(1)
    def __len__(self): return self.size

    # O(n)
    def __iter__(self):
        for X in self.A:
            yield from X

    # O(n) expected
    # expected because low probability of collision and when colliding it will traverse the linked list to insert
    # can't insert in the linked list in constant time since it will only relink the pointers?
    def build(self, X):
        for x in X: self.insert(x)

    # apply the hash function to k, using m (number of indices ?? or other divisor?)
    def _hash(self, k, m):
        return ((self.a * k) % self.p) % m

    # O(1)
    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) * 100*100 // (self.r * self.r)

    # O(n)
    def _resize(self, n):
        if (self.lower >= n) or (n >= self.upper):
            f = self.r // 100
            if self.r % 100: f+=1

            # number of stored keys?
            m = max(n, 1) * f

            # A is composed of the chains
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(k = x.key, m = m)
                A[h].insert(x)
            
            self.A = A
            self._compute_bounds()

    # O(1) e
    # expected because might take more to find in the chain, when collision occurs
    def find(self, k): 
        h = self._hash(k, len(self.A))

        # inside the chain, find(k)
        return self.A[h].find(k)
    
    # O(1) ae
    # a: amortized - might need to rebuild
    # e: expected - Low probability of collision, but if collision, traverse the chain data structure
    def insert(self, x):
        self._resize(self.size + 1)

        # apply hash
        h = self._hash(k = x.key, m = len(self.A))

        # call chain
        added = self.A[h].insert(x)

        return added
    

    # O(1) ae
    # a: might need to rebuild
    # e: might need to traverse the chain until find it 
    def delete(self, k):
        assert len(self) > 0
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        self.size -= 1
        self._resize(self.size)
        return x
    
    # O(n)
    def find_min(self):
        min = None
        for x in self:
            if (min is None) or (x.key < min.key):
                min = x
        return min
    
    # O(n)
    def find_max(self):
        max = None
        for x in self:
            if (max is None) or (x.key > max.key):
                max = x
        return max
    
    # O(n)
    def find_next(self, k):
        _next = None
        for x in self:
            if x.key > k:
                if (_next is None) or (x.key < _next.key):
                    _next = x
        return _next
    
    # O(n)
    def find_prev(self, k):
        _prev = None
        for x in self:
            if x.key < k:
                if (_prev is None) or (x.key > _prev.key):
                    _prev = x
        return _prev
    
    # O(n^2)
    def iter_order(self):
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)

if __name__ == '__main__':

