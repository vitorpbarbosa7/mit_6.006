
A = [-9,1,-5,4,3,-6,7,8,-2]
n = len(A)
memo = [(None, None) for _ in range(n)]
global_parent = [None, None]
def x(i):
    print('\nStack')
    print(A[:i])
    # breakpoint()

    #Base Case:
    #reached an empty array
    if i >= n:
        return 0, []
    
    #Subproblem and relation

    # subproblem is each one of the suffixes largest sum

    # Relation is how to from a deeper level in the stack, compute a lower level in the recurrence call
    # the trick here is that considering the A[i] as one of the options, breaks the continuity, starting a new subarray using it as the 
    # end of the array in the suffix
    # So we keep track of all the subsums
    value, subsequence = x(i+1)

    if A[i] + value > A[i]:
        # coming back in the stack, if the next value going up is good, we add it together with the subsequence returned by 
        # deeper levels in the stack 
        subsequence = [A[i]] + subsequence
    else:
        # if not, we start a new subsequence with only that value
        subsequence = [A[i]]

    memo[i] = (max(A[i], A[i] + value), subsequence) 
    print(memo)
    return memo[i]

# Original Problem:
print('\n\n Execute this shit')
x(0)
print('\n\nAnswer')
print(memo)
dict_result = dict(memo)
largest_subarray_sum = max(dict_result)
largest_subarray_values = dict_result[largest_subarray_sum]
print(largest_subarray_sum)
print(largest_subarray_values)


# possible to construct a graph of edges between them when A[i] + x(i+1) is considered
# if not considered, no edge
# then calculate the longest path 


