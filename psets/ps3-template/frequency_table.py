
        
alphabet = 'abcdefghijklmnopqrstuvwxyz'

A =  'esleastealaslatet'
B = 'tesla'
n = len(A)
k = len(B)

# get all letters that exist in A in a dict?
characters = {key: 0 for key in alphabet}

DAA = {}
# traverse with k and construct the base 26 base frequency table

for i in range(k):
    ch = A[i]
    characters[ch] += 1
    print(characters)

mykey = int(''.join(map(str, characters.values())))
print(mykey)

# DAA[frequency_mapping] += 1