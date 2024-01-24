A = 'BCDE'
B = 'FG' 

na = len(A)
nb = len(B)
memo = [[None]*nb for _ in range(na)]

def x(i, j):
    print('\nStack')
    print('Current Suffix:')
    print(f'i: {i}')
    print(f'j: {j}')
    print(f'A[i:] - {A[i:]}')
    print(f'B[j:] - {B[j:]}')

    # Base Case:
    if i == na-1 or  j == nb-1:
        return 0

    if memo[i][j] is not None:
        return memo[i][j]

    # Subproblems and relations
    if A[i] == B[j]:
        memo[i][j] = x(i+1, j+1)
        return memo[i][j]
    else:
        ed_del = 1 + x(i+1, j)
        ed_rep = 1 + x(i+1, j+1)
        ed_ins = 1 + x(i, j+1) 
        memo[i][j] = min(ed_del, ed_rep, ed_ins)
        return memo[i][j]

x(0, 0)
print(memo)
