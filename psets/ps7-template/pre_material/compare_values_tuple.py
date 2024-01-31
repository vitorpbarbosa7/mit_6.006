

A = [(34,8,71),(22, 12, 93)]

# Base Case
# get the smallest element in the last tuple 


# from going back in the stack
# get the smallest element in the current tuple which is greater than the returned in the x(i+1) 

def compare_tuple_value(i, next_values):
    previous = sorted(A[i], reverse=True)
    min_next = min(next_values)
    filtered = [num for num in previous if num > min_next]
    if len(filtered) > 0 :
        return True

def x(i):

    # Base case
    if i == len(A) - 1:
        return 1, [min(A[i])]
    
    # Relation and subproblem
    prices_day_n = sorted(A[i])
    suffix_sum, returned_subsequence = x(i+1)


    
    memo[i] = (1 + suffix_sum, [A[i]])


 

def get_element_current_tuple(i, first_element_returned_subsequence):

    previous_elements = sorted(A[i], reverse = True)

    # only elements which are greater than the first element in the returned subsequence
    filtered = [num for num in previous_elements if num > first_element_returned_subsequence]

    # from those, we always get the min value, because it is better to continue
    # to build the longest decreasing continuous subsequence from the tuples 
    return min(filtered)
