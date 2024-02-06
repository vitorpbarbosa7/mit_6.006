

# knapsack values
A = [10,8,4,5,3,7,2,6,1,9]
S = [2,3,5,7,1,4,1,6,3,8]

def dp(i, s):

    # Base Case Suffixes
    # If there are no items, we get no value from it
    if i == len(A):
        return 0, []

    # Restriction capacity
    # We can not put an item with volume greater than the available in the backpack
    if S[i] > s:
        # so keep the condition we were already there
        return dp(i+1, s)
    
    # subproblems:
    # follow for next item and keep the capacity
    local_value_not_take, returned_subsequence_take_not_take = dp(i+1, s)

    not_take_current_item = 0 + local_value_not_take

    # follow for next item and decrease capacity
    local_value_take, returned_subsequence_take = dp(i+1, s - S[i])

    take_current_item = A[i] + local_value_take
    if take_current_item > not_take_current_item:
        local_subsequence = [[A[i]]] + returned_subsequence_take 
        return take_current_item, local_subsequence

    else:
        return not_take_current_item, returned_subsequence_take_not_take

C = 10
max_value, subsequence = dp(0, C)
print(max_value)
print(subsequence)