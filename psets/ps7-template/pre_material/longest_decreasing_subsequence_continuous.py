
A = [1,2,3,4,5,6,5,4,3,2,1,8,2,6,5,4,3]

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
        memo[i] = 0 
        return -x(i+1) + x(i+1)
    
def original_problem(memo):
    return max(memo)
x(0)

max_length = original_problem(memo)

        