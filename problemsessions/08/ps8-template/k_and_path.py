import numpy as np

INF = -float('inf')

F = [['x', 'm', 'x', 'x', 't', 'm', 'm'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'm'],
            ['x', 'm', 'x', 't', 'm', 't', 't'],
            ['m', 'x', 'x', 'x', 'x', 'x', 'm'],
            ['m', 't', 'm', 'm', 't', 'x', 'x'],
            ['m', 'x', 'm', 'x', 'x', 'x', 'm'],
            ['x', 'x', 'x', 'm', 't', 'm', 'x']
]


n = len(F)
memok = [[None]*(n+1) for _ in range(n+1)]
memok[n][:] = [0]*(n+1)
for idx in range(n+1):
    memok[idx][n] = 0
# print(np.matrix(memok))
    

def indicator_mushroom(FF, ii, jj):
    return int(FF[ii][jj]=='m')
    

def k(i, j):
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
        go_right = mushroom_indicator + k(i=i, j = j+1)
        go_down = mushroom_indicator + k(i = i+1, j = j)
        memok[i][j] = max(go_right, go_down)
        return memok[i][j]

resultk = k(i=0, j = 0)
print(resultk)

# Initialize
memox = [[0]*(n+1) for _ in range(n+1)]
# Edge Base Cases
memox[n][:] = [0]*(n+1)
for idx in range(n+1):
    memox[idx][n] = 0

memox[n-1][n-1] = 1

def x(i, j):
    print(f'i: {i} and j: {j}')
    print(f'Subgrid:')
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
        memox[i][j] = 1
        return memox[i][j]
    
    #kind of found that
    if memox[i][j] != 0:
        return memox[i][j]


    mushroom_indicator = indicator_mushroom(F, i, j)    
    if F[i][j] == 't':
        # if there is a tree, we can't go there, so do not continue to explore down the path
        memox[i][j] = 0
        return memox[i][j]

    else:
        go_right = k(i, j+1)
        go_down = k(i+1, j)

        # if going right, plust where I am result in the number of necessary mushrooms, ok
        if go_right + mushroom_indicator == k(i, j):
            print('go right')
            memox[i][j] += x(i, j+1)

        if go_down + mushroom_indicator == k(i, j):
            print('go down')
            memox[i][j] += x(i+1, j)
    
    print(f'{np.matrix(memox)[i:, j:]}')
    # breakpoint()
    return memox[i][j]

# Original Problem
quick_paths = x(0, 0)
print(quick_paths)

    
