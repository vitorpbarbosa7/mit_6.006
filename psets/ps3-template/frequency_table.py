A =  'esleastealaslatet'
B = 'tesla'
n = len(A)
k = len(B)

DAA = []

# initialize hashmap with first substring sequence of lenght k
hashmap = {key: 0 for key in A}
for i in range(k):
    ch = A[i]
    hashmap[ch] += 1
# print(hashmap)

DAA.append(hashmap.copy())
# print(DAA)

# print('Initial hashmap: ', DAA[0], '\n')

for i in range(k, n):

    start_pointer = i-k
    end_pointer = i
    
    leftover_ch = A[start_pointer]
    # decrease the letter to the left
    hashmap[leftover_ch] -= 1

    ch = A[end_pointer]
    
    # increase the letter we found
    hashmap[ch] += 1

    # store the frequency table
    DAA.append(hashmap.copy())
    
    # print(f'after iteration hashmap: {hashmap}')
    # print(f'\n DAA: {DAA}')


# ------------

def _init_hashmap(sequence):
    n = len(sequence)

    hashmap = {key: 0 for key in sequence}
    for i in range(n):
        ch = sequence[i]
        hashmap[ch] += 1

    return hashmap

hashmapB = _init_hashmap(B)
print(hashmapB)
