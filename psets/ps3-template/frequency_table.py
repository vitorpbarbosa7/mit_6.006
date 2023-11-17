
def substring_count(A, B):
    # A =  'esleastealaslatet'
    # B = 'tesla'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

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

    # this does not run in O(n) because we have a fixed amount of letters in the ascii lower case english alphabet (26)
    # so this is constant time
    mykey = int(''.join(map(str, characters.values())))
    DAA[mykey] = 1

    print(DAA)
    # breakpoint()

    for i in range(k, n):

        start_pointer = i-k
        end_pointer = i
        leftover_ch = A[start_pointer]

        # decrease the letter to the left
        characters[leftover_ch] -= 1

        new_ch = A[end_pointer]

        characters[new_ch] += 1

        # this does not run in O(n) because we have a fixed amount of letters in the ascii lower case english alphabet (26)
        # so this is constant time
        mykey = int(''.join(map(str, characters.values())))
        if mykey not in DAA:
            DAA[mykey] = 1
        else:
            DAA[mykey] += 1

        print(DAA)
        # breakpoint()


    def count(DAA, B):

        characters = {key: 0 for key in alphabet}

        for i in range(k):
            ch = B[i]
            characters[ch] += 1

        Bkey = int(''.join(map(str, characters.values())))

        if Bkey in DAA:
            return DAA[Bkey]
        else:
            return
        

    return count(DAA, B)

# print(DAA)
# subs_count_B = substring_count(DAA, B)
# print(subs_count_B)



