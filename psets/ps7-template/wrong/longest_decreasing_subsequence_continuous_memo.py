

def x(i, memo, A):
    # print('Stack frame called')
    # print(f'Suffix: {A[i:]}')
    # breakpoint()

    # single element at the end
    if i == len(A)-1:
        return 1, [A[i]]
    
    # We want decreasing subsequence
    if A[i+1] < A[i]:
        suffix_sum, returned_subsequence = x(i+1, memo, A)
        memo[i] = (1 + suffix_sum, [A[i]] + returned_subsequence)
        return memo[i]
    
    else:
        # with the call of the memo[i] it will continue to update the memo array
        # even if not returned here
        # and the memo array can be used in the next level
        x(i+1, memo , A)
        memo[i] = (1, [A[i]]) 
        return memo[i]

def original_problem(memo):
    memo = dict(memo)
    max_length = max(memo)
    subsequence = memo[max_length]
    return max_length, subsequence


def lcds(A):
    memo = [(None, []) for _ in range(len(A))]
# Base case for memo
    memo[-1] = (1, [A[-1]])
    x(0, memo, A)
    max_length, subsequence = original_problem(memo)

    return max_length, subsequence

if __name__ == '__main__':

    A = [1,2,3,3,4,5,6,5,4,3,2,1,8,2,6,5,4,3]
    # A = [19,17,10,5,4]

    max_length, subsequence = lcds(A)
    print(max_length)
    print(subsequence)