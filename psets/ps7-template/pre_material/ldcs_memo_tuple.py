




def convert_prices(input, n, k):

    result = []
    for i in range(0, len(input), k):
        result.append(input[i:i+k])

    return result

inputA = ((12, 19, 7, 17, 5, 10, 5, 25, 4, 20), 5, 2)
A = convert_prices(*inputA)
print(A)

inputA = ((13, 25, 14, 2, 9, 17, 16, 13, 10, 16), 5, 2)
A = convert_prices(*inputA)
print(A)

def compare_tuple_value(i):
    greater = []
    for previous_element in A[i]:
        for next_element in A[i+1]:
            greater.append(previous_element > next_element)
    return max(greater)

def get_element_current_tuple(i, first_element_returned_subsequence):
    # previous_elements = sorted(A[i], reverse = True)
    # only elements which are greater than the first element in the returned subsequence
    previous_elements = A[i]
    print(previous_elements)
    print(first_element_returned_subsequence)
    breakpoint()
    filtered = [num for num in previous_elements if num > first_element_returned_subsequence]
    # maybe going up in the stack, in the way the numbers were chosen, there is no element here
    if len(filtered) == 0:
        return
    # from those, we always get the min value, because it is better to continue
    # to build the longest decreasing continuous subsequence from the tuples
    return min(filtered)

memo = [(None, []) for _ in range(len(A))]
# Base case for memo
memo[-1] = (1, [min(A[-1])])
def x(i):
    print('Stack frame called')
    print(f'Suffix: {A[i:]}')
    # breakpoint()

    # single element at the end
    if i == len(A)-1:
        return 1, [min(A[i])]
    
    # We want decreasing subsequence
    # if A[i+1] < A[i]:
    # this function is needed to go down in the stack, in the suffix way 
    if compare_tuple_value(i):
        suffix_sum, returned_subsequence = x(i+1)
        first_element_returned_subsequence = returned_subsequence[0]
        element_from_current_tuple = get_element_current_tuple(i, first_element_returned_subsequence)
        if element_from_current_tuple is not None:
            memo[i] = (1 + suffix_sum, [element_from_current_tuple] + returned_subsequence)
            return memo[i]
        # even if when going down in the stack with the (compare_tuple_value(i)) there was a bigger element
        # when going back, going up in the stack, the element we chose maybe is greater than the element in the current level
        # so we invoke the case in which we start forming a new stack
        else:
            # with the call of the memo[i] it will continue to update the memo array
            # even if not returned here
            # and the memo array can be used in the next level

            # no need to go down in the stack again ?
            # x(i+1)
            # if we have not found any element in the current tuple which is greater than any element in the next tuple
            # it means we can use the min of the current tuple to try building for next ones
            memo[i] = (1, [min(A[i])]) 
            return memo[i]
    
    else:
        # with the call of the memo[i] it will continue to update the memo array
        # even if not returned here
        # and the memo array can be used in the next level
        x(i+1)
        # if we have not found any element in the current tuple which is greater than any element in the next tuple
        # it means we can use the min of the current tuple to try building for next ones
        memo[i] = (1, [min(A[i])]) 
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