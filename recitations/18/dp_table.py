# knapsack values
A = [10, 8, 4, 5, 3, 7, 2, 6, 1, 9]
S = [2, 3, 5, 7, 1, 4, 1, 6, 3, 8]

# Memoization table
memo = {}

def dp(i, s):
    # Base Case Suffixes
    if i == len(A):
        return 0, []

    # Check if the result is already memoized
    if (i, s) in memo:
        return memo[(i, s)]

    # Restriction capacity
    if S[i] > s:
        result = dp(i + 1, s)
    else:
        # Subproblem: Do not take the current item
        local_value_not_take, returned_subsequence_not_take = dp(i + 1, s)

        # Subproblem: Take the current item
        local_value_take, returned_subsequence_take = dp(i + 1, s - S[i])
        take_current_item = A[i] + local_value_take

        # Compare and choose the better option
        if take_current_item > local_value_not_take:
            local_subsequence = [[A[i]]] + returned_subsequence_take
            result = take_current_item, local_subsequence
        else:
            result = local_value_not_take, returned_subsequence_not_take

    # Memoize the result
    memo[(i, s)] = result
    return result

C = 10
max_value, subsequence = dp(0, C)
print("Max Value:", max_value)
print("Subsequence:", subsequence)