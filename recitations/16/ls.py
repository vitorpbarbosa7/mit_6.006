from visualiser.visualiser import Visualiser as vs

A = [-2, 3, -1, 5, -4]
n = len(A)

memo = [None] * n

@vs(node_properties_kwargs={"shape":"record", "color":"#00cc99", "style":"filled", "fillcolor":"#e6ffe6"})
def max_subarray_sum(k):
    suffix = A[k:]
    print(f'\nStack frame: k={k}, suffix={suffix}')

    # Base Case
    if k == n - 1:
        memo[k] = A[k]
        print(f"Base case memo[{k}] = {memo[k]}")
        return memo[k]

    # Memoization Check
    if memo[k] is not None:
        print(f"Memoized memo[{k}] = {memo[k]} (reused)")
        return memo[k]

    # Recursive step (relation)
    next_value = max_subarray_sum(k + 1)
    memo[k] = max(A[k], A[k] + next_value)

    print(f"Computed memo[{k}] = {memo[k]} (max({A[k]}, {A[k]} + {next_value}))")
    return memo[k]

# Solve original problem clearly
max_sum = float('-inf')
for k in range(n):
    current_max = max_subarray_sum(k)
    max_sum = max(max_sum, current_max)
    print(f"Max sum after k={k}: {max_sum}, Memo: {memo}")

print("\nFinal Max Subarray Sum:", max_sum)

# Generate the recursion tree visualization clearly
vs.make_animation("max_subarray_sum_tree.gif", delay=2)
