
A = 'CARBOHYDRATE'
# A = 'EFAGBCD'

n = len(A)
def x(i):
    print('\nStack frame created')
    print(f'Suffix to use brute force with others: {A[i:]}')
    # breakpoint()
    # Base case
    # the index makes the suffix reaches its end
    if i == n:
        return 0

    lis_js = [0]*(n)
    for j in range(i, n, 1):
        print(f'Compare {A[i]} and {A[j]}')
        # breakpoint()
        # para ser considerado subsequence 
        # elemento anterior deve ser menor que o proximo elemento 
        # logo fazemos brute force para ver se comecando com a letra i
        # quais sao as subsequences existentes
        if A[j] > A[i]:
            print(f'Found {A[j]} greather than {A[i]}')
            # and for j, how many can I put on top of each, after it?
            # that will respect that the first i goes before, than j, than we found from j, what can go after this j, using the recursion itself
            # and at the end of this recursion call we return that it is 1 (current i) + maximum number of less than, which is marked in the lis_js
            lis_js[j] = x(j)

    # we enforce that i is in the answer, maybe the longest increasing subsequence will not have
    # any more element, but i will be there 
    # in the recursion call it will only increase if we find that A[i] < A[j]
    # that is, for a single i, we will check which items are greater than j
    return 1 + max(lis_js)

def original_problem():

    all_lengths = []
    for i in range(n):
        all_lengths.append(x(i))

    return max(all_lengths)

length = original_problem()
print(length)