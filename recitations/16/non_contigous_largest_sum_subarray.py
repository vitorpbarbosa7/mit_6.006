
A = [-9,1,-5,4,3,-6,7,8,-2]
n = len(A)
def x(i):

    #Base Case:
    #reached an empty array
    if i >= n:
        return 0
    
    #Subproblem and relation

    # subproblem is each one of the suffixes largest sum

    # Relation is how to from a deeper level in the stack, compute a lower level in the recurrence call
    return max(A[i] + x(i+1), x(i+1), 0)

# Original Problem:
largest_sum_subarray = x(0)
print(largest_sum_subarray)


