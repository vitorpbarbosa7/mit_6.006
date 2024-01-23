
A = [-9,1,-5,4,3,-6,7,8,-2]
# bottom up implementation:
def max_subarray_sum(A):
    # memo, keep track of each prefix solution
    x = [None for _ in A]
    # Base Case, for prefix
    x[0] = A[0]
    print('\n')
    print(A)
    print(x)
    for k in range(1, len(A)):
        # go increasing the prefix
        # use the previously calculated max of the prefix x[k-1]
        # to calculate the max from prefix x[k]
        x[k] = max(A[k], A[k] + x[k-1])
        print('\n')
        print(A[k:])
        print(x)
    return max(x)

largest_sum_subarray = max_subarray_sum(A)
print(largest_sum_subarray)


# It is doing something like this:
# when a dot replaces all previous underscores, means a new subarray will start, with only that element, because it was better
# to keep only him and try others, then keep the sum of him with others
# each row corresponds to a k we kept track of 
# _
# _ _ 
# . . _
# . . _ _
# . . _ _ _ 
# . . . . . _