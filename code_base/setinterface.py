class Seq:
    def __init__(self):
        self.S = []
        self.size = 0

    def build(self, A):
        self.S = A
        self.size = len(A)

    def len(self):
        return self.size

    def iter_seq(self):
        for x in self.S:
            yield x

    def get_at(self, i):
        return self.S[i]

    def set_at(self, i, x):
        self.S[i] = x

    def insert_at(self, i, x):
        self.S.insert(i, x)
        self.size += 1

    def delete_at(self, i):
        deleted = self.S.pop(i)
        self.size -= 1
        return deleted

    def insert_first(self, x):
        self.S.insert(0, x)
        self.size += 1

    def delete_first(self):
        deleted = self.S.pop(0)
        self.size -= 1
        return deleted

    def insert_last(self, x):
        self.S.append(x)
        self.size += 1

    def delete_last(self):
        deleted = self.S.pop()
        self.size -= 1
        return deleted
        

class SetFromSeq(Seq):
        
    def __init__(self): 
        super().__init__()
    
    def __len__(self):  return len(self.S)
    
    def __iter__(self): yield from self.S

    def build(self, A):
        super().build(A)

    def insert(self, x):

        for i in range(len(self.S)):
            if self.S.get_at(i).key == x.key:
                self.S.set_at(i, x)
                return 
        self.insert_last(x)

    def delete(self, k):
        
        for i in range(len(self.S)):
            if self.S.get_at(i).key == k:
                return self.S.delete_at(i)
            
    def find_min(self):
        current_min = None
        
        for x in self:
            if (current_min is None) or (x.key < current_min.key):
                current_min = x

        return current_min
    
    def find_max(self):
        current_max = None
        for x in self:
            if (current_max is None) or (x.key > current_max.key):
                current_max = x
        return current_max
    

    def find_next(self, k):
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return x
    
    def find_prev(self, k):
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key > out.key):
                    out = x
        return x
    
    def iter_ord(self):
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key) 

# Example usage:
if __name__ == "__main__":
    set_from_seq = SetFromSeq()
    set_from_seq.build([(1, 'a'), (2, 'b'), (3, 'c')])

    for item in set_from_seq.iter_ord():
        print(item)