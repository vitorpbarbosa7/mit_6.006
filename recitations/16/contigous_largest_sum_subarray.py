
A = [-9,1,-5,4,3,-6,7,8,-2]
n = len(A)
memo = [None for _ in range(n)]
def x(i):

    #Base Case:
    #reached an empty array
    if i >= n:
        return 0
    
    #Subproblem and relation

    # subproblem is each one of the suffixes largest sum

    # Relation is how to from a deeper level in the stack, compute a lower level in the recurrence call
    # the trick here is that considering the A[i] as one of the options, breaks the continuity, starting a new subarray using it as the 
    # end of the array in the suffix
    # So we keep track of all the subsums
    memo[i] = max(A[i], A[i] + x(i+1))
    return memo[i]

# Original Problem:
x(0)
print(memo)
# largest_sum_subarray
# print(largest_sum_subarray)


