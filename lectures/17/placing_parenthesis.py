# https://gist.github.com/definito/9abb5b9146286f5dda9d1854cb7c4195

import math
def calc(a, b, op):

    print(a,op,b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def MinAndMax(M, m, i, j, operators):

    min_value = math.inf
    max_value = -math.inf
    # Different placements of the parenthesis
    for k in range(i, j):
        print(f'i:{i} - k:{k} - k+1:{k+1} - j:{j}')
        print(f'M-M: {M[i][k]} : {M[k+1][j]}')
        print(f'M-m: {M[i][k]} : {m[k+1][j]}')
        print(f'm-M: {m[i][k]} : {M[k+1][j]}')
        print(f'm-m: {m[i][k]} : {m[k+1][j]}')
        breakpoint()
        a = calc(M[i][k], M[k+1][j], operators[k])
        b = calc(M[i][k], m[k+1][j], operators[k])
        c = calc(m[i][k], M[k+1][j], operators[k])
        d = calc(m[i][k], m[k+1][j], operators[k])
        print(min_value)
        print(max_value)
        print(a, b, c, d)
        # max value may have been from a value which used min_value
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
        print(min_value)
        print(max_value)
        # breakpoint()
    return min_value, max_value


expression = [7,'+',-4, '*',3,'+',-5]
operators, operands = [], []

for i in expression:
    if i in ['+', '-', '*']:
        operators.append(i)
    else:
        operands.append(int(i))

n = len(operands)
m = [[None for x in range(n)] for x in range(n)]
# breakpoint()
M = [[None for x in range(n)] for x in range(n)]
# breakpoint()

# Base case, main diagonal 
for i in range(n):
    m[i][i] = operands[i]
    M[i][i] = operands[i]
# breakpoint()

for s in range(1, n):
    for i in range(0, n-s):
        j = i + s
        print(f'Current substring: {operands[i:j]}')
        # breakpoint()
        m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)
        print(m)
        print(M)

print(M[0][n-1])

