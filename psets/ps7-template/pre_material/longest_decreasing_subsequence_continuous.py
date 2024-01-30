
A = [1,2,3,3,4,5,6,5,4,3,2,1,8,2,6,5,4,3]

memo = [None]*len(A)
memo[-1] = 1
def x(i):
    print('Stack frame called')
    print(f'Suffix: {A[i:]}')

    # single element at the end
    if i == len(A)-1:
        return 1
    
    if memo[i] is not None:
        return memo[i] 

    # We want decreasing subsequence
    if A[i+1] < A[i]:
        memo[i] = 1 + x(i+1)
        return memo[i]
    
    else:
        # with the call of the memo[i] it will continue to update the memo array
        # even if not returned here
        # and the memo array can be used in the next level
        x(i+1)
        memo[i] = 1 
        return memo[i]
    
def original_problem(memo):
    return max(memo)
x(0)

max_length = original_problem(memo)

        