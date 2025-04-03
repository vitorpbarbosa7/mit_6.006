

# knapsack values
A = [10,8,4,5,3,7,2,6,1,9]
S = [2,3,5,7,1,4,1,6,3,8]

def dp(i, s):

    # Base Case Suffixes
    # If there are no items, we get no value from it
    if i == len(A):
        return 0

    # Restriction capacity
    # We can not put an item with volume greater than the available in the backpack
    if S[i] > s:
        # so keep the condition we were already there
        return dp(i+1, s)
    
    # subproblems:
    # guessing, brute forcing
    # follow for next item and keep the capacity (do not take the item )
    not_take_current_item = 0 + dp(i+1, s)

    # follow for next item and decrease capacity (take the item)
    take_current_item = A[i] + dp(i+1, s - S[i])

    local_max = max(not_take_current_item, take_current_item)

    return local_max

C = 10
max_value = dp(0, C)
print(max_value)