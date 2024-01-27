from visualiser.visualiser import Visualiser as vs

INF = -float('inf')

F = [
    ['x', 'x', 't', 'x', 'm'],
    ['x', 'x', 'x', 'x', 'x'],
    ['m', 'm', 'x', 'x', 'm'],
    ['x', 'x', 't', 'm', 't'],
    ['x', 't', 'x', 'm', 'x'],
]



n = len(F)
memok = [[None]*(n+1) for _ in range(n+1)]
memok[n][:] = [0]*(n+1)
for ii in range(n+1):
    memok[ii][n] = 0
# print(np.matrix(memok))
    
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
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

    mushroom_indicator = int(F[i][j]=='m') 
    # Number of mushrooms she will get from this level if there is a tree
    # if there is a tree, she can't neve go here, so this will help in the max function 
    if F[i][j] == 't':
        memok[i][j] = INF
        return memok[i][j]
    
    else:
        go_right = mushroom_indicator + k(i=i, j = j+1)
        go_left = mushroom_indicator + k(i = i+1, j = j)
        memok[i][j] = max(go_right, go_left)
        return memok[i][j]

k(i=0, j = 0)
vs.make_animation("k_mushrooms", delay=2)