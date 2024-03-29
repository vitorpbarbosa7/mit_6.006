import numpy as np

INF = -float('inf')

def indicator_mushroom(FF, ii, jj):
    return int(FF[ii][jj]=='m')

def testk(F):
    n = len(F)
    memok = [[None]*(n+1) for _ in range(n+1)]
    memok[n][:] = [0]*(n+1)
    for ii in range(n+1):
        memok[ii][n] = 0
    # print(np.matrix(memok))
        
    # Initialize
    memox = [[0]*(n+1) for _ in range(n+1)]
    # Edge Base Cases
    memox[n][:] = [0]*(n+1)
    for idx in range(n+1):
        memox[idx][n] = 0

    resultk = k(i=0, j = 0, memok = memok, n = n, F = F)
    # print(np.matrix(memok))
    print(resultk)

    # Original Problem
    quick_paths = x(0, 0, memox, n, F, memok)
    print(quick_paths)
    

def k(i, j, memok, n, F):
    # print(f'i: {i} and j: {j}')
    # print(f'Subgrid:')
    # print(f'{np.matrix(F[i:][j:])}')
    # breakpoint()

    # Base Cases
    if i == n-1 and j == n-1:
        memok[i][j] = 0
        return memok[i][j]
    if memok[i][j] is not None:
        return memok[i][j]

    mushroom_indicator = indicator_mushroom(F, i, j)
    # Number of mushrooms she will get from this level if there is a tree
    # if there is a tree, she can't neve go here, so this will help in the max function 
    if F[i][j] == 't':
        memok[i][j] = INF
        return memok[i][j]
    
    else:
        go_right = mushroom_indicator + k(i=i, j = j+1, memok=memok, n=n, F=F)
        go_down = mushroom_indicator + k(i = i+1, j = j, memok=memok, n=n, F=F)
        memok[i][j] = max(go_right, go_down)
        return memok[i][j]


def x(i, j, memox, n, F, memok):
    # print(f'i: {i} and j: {j}')
    # print(f'Subgrid:')
    # print(f'{np.matrix(F)[i:, j:]}')
    # breakpoint()

    # The subproblem will be the number of quick paths starting from i, j which have
    # exactly the memok[i][j]
    # we calculated before

    # Base Case:
    # Last little guy is considered a grid, so will be considered 1
    if i == n:
        memox[i][j] = 0
        return memox[i][j]
    if j == n:
        memox[i][j] = 0
        return memox[i][j]

    if i == n-1 and j == n-1:
        return 1
    
    # what avoids summing paths for paths already calculated
    if memox[i][j] != 0:
        return memox[i][j]

    mushroom_indicator = indicator_mushroom(F, i, j)    
    if F[i][j] == 't':
        # if there is a tree, we can't go there, so do not continue to explore down the path and return no grid
        memox[i][j] = 0
        return memox[i][j]

    else:
        go_right = memok[i][j+1]
        go_down = memok[i+1][j]

        # if going right, plust where I am result in the number of necessary mushrooms, ok
        if go_right + mushroom_indicator == memok[i][j]:
            # print('go right')
            memox[i][j] += x(i, j+1, memox, n, F, memok)

        if go_down + mushroom_indicator == memok[i][j]:
            # print('go down')
            memox[i][j] += x(i+1, j, memox, n, F, memok)

    return memox[i][j]
    
from tests import tests

for input, _ in tests:
     testk(F = input)

