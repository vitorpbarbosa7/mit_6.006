class Anagram:
    
    def __init__(self):
        self.hashmap = None
    
    def build(self, A):
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
        


