A = 'HIEROGLYPHOLOGY'
B = 'MICHAELANGELO'

A = 'HABIT'
B = 'THEIR'

def x(i, j, memo):
    # Base Case:
    if i >= len(A) or j >= len(B):
        return 0

    # If the result is already memoized, return it
    if memo[i][j] != -1:
        return memo[i][j]

    # Relation:
    if A[i] == B[j]:
        # If characters match, include them in the LCS
        memo[i][j] = 1 + x(i + 1, j + 1, memo)
    else:
        # If characters don't match, exclude one and consider the maximum length
        memo[i][j] = max(x(i + 1, j, memo),
                         x(i, j + 1, memo))

    return memo[i][j]

# Initialize memoization table with -1
memoization_table = [[-1] * len(B) for _ in range(len(A))]
print(memoization_table)

# Call the function with the starting indices
lcs_length = x(0, 0, memoization_table)
print(memoization_table)

print("Length of Longest Common Subsequence:", lcs_length)