from arrayseq import ArraySeq

class E:
    def __init__(self, key):
        self.key = key
    def __repr__(self):
        return str(self.key)

class SetFromSeq(ArraySeq):
        
    def __init__(self): 
        self.S = ArraySeq()
    
    def __repr__(self):
        return ', '.join(str(x) for x in self)
    
    def __len__(self):  
        return len(self.S)
    
    # the clever way to make the iterable of self be the same as self.S ArraySeq
    def __iter__(self): 
        yield from self.S

    def build(self, A):
        self.S.build(A)
    
    # O(n)
    # from self.S elements, iterate over and check the key, if the key is equal to some already existing key
    # insert it 
    # if not, insert at last
    def insert(self, x):

        for i in range(len(self)):
            if self.S.get_at(i).key == x.key:
                self.S.set_at(i, x)
                return 
        self.S.insert_last(x)
    
    # O(n)
    # again, iterate over, find the key, when key is found, them delete it 
    def delete(self, k):
        
        for i in range(len(self.S)):
            if self.S.get_at(i).key == k:
                return self.S.delete_at(i)
        
    # O(n)
    # very simple, iterate over, keep track of some, use comparison model to compare them, then return the min 
    def find_min(self):
        current_min = None
        
        for x in self.S:
            if (current_min is None) or (x.key < current_min.key):
                current_min = x

        return current_min
    
    # O(n)
    # equal to find_min
    def find_max(self):
        current_max = None
        for x in self.S:
            if (current_max is None) or (x.key > current_max.key):
                current_max = x
        return current_max
    
    # O(n)
    # iterate over again
    def find_next(self, k):
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return out
    
    def find_prev(self, k):
        out = None
        for x in self:
            if x.key < k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out
    
    # go always finding the smallest one from the current one
    def iter_ord(self):
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key) 

if __name__ == '__main__':
     
    sfs = SetFromSeq()
    elements = [5,5,3,4,2,1]
    X = [E(x) for x in elements]

    sfs.build(X)
    print(sfs)

    sfs.insert(E(10))
    print(sfs)

    sfs.delete(E(5))
    print(sfs)

    _min = sfs.find_min()    
    print(_min)

    _max = sfs.find_max()
    print(_max)

    _next = sfs.find_next(2)
    print(_next)

    _prev = sfs.find_prev(4)
    print(_prev)
    
    print('passou aqui')
    ord_elements = [x for x in sfs.iter_ord()]
    print(ord_elements)