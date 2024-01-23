A = 'EFAGBCD'
n = len(A)

# Global variable to store the longest subsequence
longest_subsequence = []

def x(i):
    global longest_subsequence
    print('\nStack frame created')
    print(f'Suffix to use brute force with others: {A[i:]}')
    
    # Base case
    # the index makes the suffix reaches its end
    if i == n:
        return 0, []

    lis_js = [0] * n
    for j in range(i, n, 1):
        print(f'Compare {A[i]} and {A[j]}')

        # para ser considerado subsequence 
        # elemento anterior deve ser menor que o proximo elemento 
        # logo fazemos brute force para ver se comecando com a letra i
        # quais sao as subsequences existentes
        if A[i] < A[j]:
            print(f'Found {A[j]} greater than {A[i]}')
            length, subsequence = x(j)
            lis_js[j] = (length, subsequence)

    # Check if lis_js has no non-zero elements
    if all(elem == 0 for elem in lis_js):
        result = (0, [])
    else:
        # we enforce that i is in the answer, maybe the longest increasing subsequence will not have
        # any more element, but i will be there 
        # in the recursion call it will only increase if we find that A[i] < A[j]
        # that is, for a single i, we will check which items are greater than j
        max_length = max((x for x in lis_js if x[0] != 0), key=lambda x: x[0])
        result = (1 + max_length[0], [A[i]] + max_length[1])
    
    # Update longest_subsequence if the current result has a longer length
    if result[0] > len(longest_subsequence):
        longest_subsequence = result[1]
    
    return result

def original_problem():
    global longest_subsequence
    all_lengths = []
    
    for i in range(n):
        all_lengths.append(x(i))
    
    return longest_subsequence

longest_subseq = original_problem()
print(f'Longest subsequence: {longest_subseq}')
