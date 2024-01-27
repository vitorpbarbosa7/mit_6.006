INF = -float('inf')

def count_paths(F):
    '''
    Input:  F | size-n direct access array of size-n direct access arrays
              | each F[i][j] is either 't', 'm', or 'x'
              | for tree, mushroom, empty respectively
    Output: m | the number of distinct optimal paths in F
              | starting from (0,0) and ending at (n-1,n-1)
    '''
    p = 0
    n = len(F)
    memok = [[None]*n for _ in range(n)] 

    def k(i, j):

        # Base Case
        if i == n-1 and j == n-1:
            memok[i][j] = 0
            return memok[i][j]

        mushroom_indicator = int(F[i][j]=='m') 
        # Number of mushrooms she will get from this level if there is a tree
        # if there is a tree, she can't neve go here, so this will help in the max function 
        if F[i, j] == 't':
            memok[i][j] = INF
            return memok[i][j]
        
        else:
            go_right = mushroom_indicator + k(i, j+1)
            go_left = mushroom_indicator + k(i+1, j)
            memok[i][j] = max(go_right, go_left)
            




    
    return p
