
# Example usage:
expression = [2, '*', -3, '+', 5, '*', -4, '+', -6]
n = len(expression)

# Initialize memoization table
memo = {}

def dp(i, j, opt):
    print('stack frame called')
    print(f'i: {i}, j: {j}, opt: {opt}')
    # breakpoint()
    # Base case: Only one number, no operations left
    if i == j - 1:
        return int(expression[i])

    # Check if result is already memoized
    if (i, j, opt) in memo:
        return memo[(i, j, opt)]

    # Initialize result based on opt
    if opt == 'max':
        result = float('-inf')
    else:
        result = float('inf')

    # Iterate over possible locations of outermost parentheses/last operation
    for k in range(i + 1, j, 2):
        left_value = dp(i, k, 'max')
        right_value = dp(k + 1, j, 'max' if opt == 'max' else 'min')

        # Calculate value based on operator
        if expression[k] == '+':
            current_value = left_value + right_value
        elif expression[k] == '*':
            current_value = left_value * right_value

        # Update result based on opt
        if opt == 'max':
            result = max(result, current_value)
        else:
            result = min(result, current_value)

    # Memoize the result
    memo[(i, j, opt)] = result
    return result


# Calculate the maximum result for the entire expression
max_result = dp(0, n, 'max')
print(max_result)

# result = arithmetic_parenthesization(expression)
# print("Maximum evaluated value:", result)
