class Anagram:
    
    def __init__(self):
        self.hashmap = None
        self.A = None
        self.Bs = None
        self.k = None
    
    def build(self, A, Bs):
        self.k = len(Bs[0])
        self.hashmap = {key: 0 for key in A}
        self.string_sequence = [character for character in A]

    def substring_count(self, B):
        pass

    def _directaccessarray(self):
        DAA = 


if __name__ == '__main__':

    A =  'esleastealaslatet'
    B = 'tesla'

    anagram = Anagram()
    anagram.build(A)
    print(anagram.hashmap)
        


