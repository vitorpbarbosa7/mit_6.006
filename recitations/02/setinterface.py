
class Seq:

    def __init__(self, ):
        self.S = []
        self.size = 0

    def build():
        pass

    def len():
        pass

    def iter_seq():
        pass

    def get_at(i):
        pass

    def set_at(i, x):
        pass

    def insert_at(i, x):
        pass

    def delete_at(i):
        pass

    def insert_first(x):
        pass

    def delete_first():
        pass

    def insert_last(x):
        pass

    def delete_last():
        pass
        
        

class SetFromSeq(Seq):
        
    def __init__(self): 
        super.__init__()
    
    def __len__(self):  return len(self.S)
    
    def __iter__(self): yield from self.S

    def build(self, A):
        self.S.build(A)

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

    