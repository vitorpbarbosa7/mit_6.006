




def convert_prices(input, n, k):

    result = []
    for i in range(0, len(input), k):
        result.append(input[i:i+k])

    return result

inputA = ((13, 25, 14, 2, 9, 17, 16, 13, 10, 16), 5, 2)
A = convert_prices(*inputA)
print(A)
breakpoint()

memo = [(None, []) for _ in range(len(A))]
# Base case for memo
memo[-1] = (1, [A[-1]])
def x(i):
    print('Stack frame called')
    print(f'Suffix: {A[i:]}')
    # breakpoint()

    # single element at the end
    if i == len(A)-1:
        return 1, [A[i]]
    
    # We want decreasing subsequence
    if A[i+1] < A[i]:
        suffix_sum, returned_subsequence = x(i+1)
        memo[i] = (1 + suffix_sum, [A[i]] + returned_subsequence)
        return memo[i]
    
    else:
        # with the call of the memo[i] it will continue to update the memo array
        # even if not returned here
        # and the memo array can be used in the next level
        x(i+1)
        memo[i] = (1, [A[i]]) 
        return memo[i]

def original_problem(memo):
    memo = dict(memo)
    max_length = max(memo)
    subsequence = memo[max_length]
    return max_length, subsequence
x(0)

max_length, subsequence = original_problem(memo)
print(max_length)
print(subsequence)