
expression = [7,'+',4, '*',3,'+',5]
operators, operands = [], []
for i in expression:
    if i in ['+', '-', '*']:
        operators.append(i)
    else:
        operands.append(int(i))
n = len(operands)
memo = [[None]*n for _ in range(n)]

def calc(a, b, op):

    print(a,op,b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def x(i,j):
    print(f'i: {i}, j: {j}')

    # Base case, single numbers
    if i == j:
        memo[i][j] = operands[i]
        return memo[i][j]

    if memo[i][j] is not None:
        return memo[i][j]

    if isinstance(operands[j], str):
        return -float('inf')

    # Relate
    max_value = -float('inf')
    for k in range(i,j, 1):
        x_left = x(i, k)
        x_right = x(k+1, j)
        calc_value = calc(x_left, x_right, operands[k])
        max_value = max(max_value, calc_value)

    return max_value 

for i in range(0, n-1, 1):
    for j in range(n-1, i, -1):
        memo[i][j] = x(i, j)

print(memo)




