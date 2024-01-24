import numpy as np

A = 'BCDE'
B = 'FG' 

na = len(A)
nb = len(B)
memo = [[None]*nb for _ in range(na)]

# Initialize base cases for the last column
for i in range(na-2, -1, -1):
    memo[i][nb-1] = memo[i+1][nb-1] + 1

# Initialize base cases for the last row
for j in range(nb-2, -1, -1):
    memo[na-1][j] = memo[na-1][j+1] + 1

def x(i, j):
    print('\nStack')
    print('Current Suffix:')
    print(f'i: {i}')
    print(f'j: {j}')
    print(f'A[i:] - {A[i:]}')
    print(f'B[i:] - {B[j:]}')
    print(np.matrix(memo))
    breakpoint()

    # Base Case:
    if i == na or  j == nb:
        return 0

    if memo[i][j] is not None:
        return memo[i][j]    

    print(A)
    print(B)
    # Subproblems and relations
    if A[i] == B[j]:
        memo[i][j] = x(i+1,j+1)
        return memo[i][j]
    else:
        ed_del = 1 + x(i+1, j)
        ed_rep = 1 + x(i+1,j+1)
        ed_ins = 1 + x(i, j+1) 
        memo[i][j] = min(ed_del, ed_rep, ed_ins)
        return memo[i][j]


result = x(0,0)
print(np.array(memo))
print(result)