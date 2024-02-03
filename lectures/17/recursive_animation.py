
from visualiser.visualiser import Visualiser as vs
# Example usage:
numbers = [7, -4, 3, -5]
operators = ['+', 'x', '+']
n = len(numbers)

# Initialize memoization tables for maximum and minimum values
memo_max = [[None] * n for _ in range(n)]
memo_min = [[None] * n for _ in range(n)]

@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def dp(i, j, is_max):
    # Base case: Single number
    if i == j:
        return numbers[i]

    # Check if result is already memoized
    if is_max and memo_max[i][j] is not None:
        return memo_max[i][j]
    elif not is_max and memo_min[i][j] is not None:
        return memo_min[i][j]

    # Initialize result based on is_max
    result = float('-inf') if is_max else float('inf')

    # Iterate over possible locations of splitting the subexpression
    for k in range(i, j):
        op = operators[k]

        # Calculate value based on operator
        if op == '+':
            current_value = dp(i, k, is_max) + dp(k + 1, j, is_max)
        elif op == 'x':
            current_value = dp(i, k, is_max) * dp(k + 1, j, is_max)

        # Update result based on is_max
        if is_max:
            result = max(result, current_value)
        else:
            breakpoint()
            result = min(result, current_value)

    # Memoize the result
    if is_max:
        memo_max[i][j] = result
    else:
        memo_min[i][j] = result
    

    return result

# Calculate the maximum result for the entire expression
dp(0, n - 1, True)
vs.make_animation("lis_parenthesis.gif", delay=2)
# max_result = dp(0, n - 1, True)
# print(max_result)

# # result = maximize_expression_value(numbers, operators)
# print("Maximum evaluated value:", max_result)
