
import numpy as np
def x(i, memo, A, big_memo):
    print('\nStack frame created')
    print(f'Suffix to use brute force with others: {A[i:]}')
    # breakpoint()
    # Base case
    # the index makes the suffix reaches its end
    n = len(A)
    if i == n:
        base_case_count = 0
        base_case_subsequence = []
        return (base_case_count, base_case_subsequence)

    lis_js = [(0, [])]*n
    for j in range(i, n, 1):
        if memo[i][j][0] != 0:
            count, subsequence = memo[i][j]
            lis_js[j] = (count, subsequence)

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
            jcount, jsub = x(j, memo , A, big_memo)
            memo[i][j] = (jcount, jsub)
            lis_js[j] = (jcount, jsub)

    # we enforce that i is in the answer, maybe the longest increasing subsequence will not have
    # any more element, but i will be there 
    # in the recursion call it will only increase if we find that A[i] < A[j]
    # that is, for a single i, we will check which items are greater than j
    count_sequence_dict = dict(lis_js)
    largest_lis_without_i = max(count_sequence_dict)
    largest_subsequence_without_i = count_sequence_dict[largest_lis_without_i]
    count = 1 + largest_lis_without_i
    subsequence = [A[i]] + largest_subsequence_without_i
    big_memo[i] = (count, subsequence)
    print(big_memo)
    # breakpoint()
    return  (count, subsequence)

def original_problem(A, memo, big_memo):
    all_lengths, all_subsequences = [], []
    n = len(A)
    for i in range(n):
        single_length, single_subsequence = x(i, memo, A, big_memo)
        all_lengths.append(single_length)
        all_subsequences.append(single_subsequence)

    dict_result = {k: v for k,v in zip(all_lengths, all_subsequences)}

    max_length = max(dict_result)
    max_subsequence = dict_result[max_length]

    return max_length, max_subsequence

def lis(A):
    big_memo = [(0, [])]*len(A)
    memo = [[(0, [])]*len(A) for _ in range(len(A))]
    final_length, final_subsequence = original_problem(A, memo, big_memo)
    return final_length, final_subsequence
    
if __name__ == '__main__':
    A = 'CARBOHYDRATE'
    final_length, final_subsequence = lis(A)
    print(final_length)
    print(final_subsequence)