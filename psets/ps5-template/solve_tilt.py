def solve_tilt(B, t):
    '''
    Input:  B | Starting board configuration
            t | Tuple t = (x, y) representing the target square
    Output: M | List of moves that solves B (or None if B not solvable)
    '''
    M = []
    
    def neighbors(config):
        MOVES = ['up','down','left','right']
        register_moves = {}
        for m in MOVES:
            new_config = move(config, m)
            # print(f'\n New neighbor from move {m}:')
            # print(S)
            # print(board_str_double(config, new_config, m))
            # breakpoint()
            register_moves[new_config] = m

        return register_moves

    def explore_frontier(frontier, parent):

        new_frontier = []
        # explore one frontier of configurations
        # creating other frontier with new configurations
        for config in frontier:
            _neighbors = neighbors(config)
            for new_config, move in _neighbors.items():
                if new_config not in parent:
                    # from the config, the move was {move} to get to the new_config
                    parent[new_config] = [config, move]
                    new_frontier.append(new_config)

        return new_frontier

    def check_solved(config, t):
        # column x
        x = t[0]
        # row y
        y = t[1]
        if config[y][x] == 'o':
            return True 
        return False    

    def unweighted_shortest_path(
        source_config, 
        destination_config, 
        parent
        ):

        current_config = destination_config
        moves = []
        while current_config != source_config:
            # Backtrack in the graph
            list_single_node_backtrack = parent[current_config]
            print(list_single_node_backtrack)
            # breakpoint()
            current_config = list_single_node_backtrack[0]
            current_move = list_single_node_backtrack[1]

            moves.append(current_move)
            print(f'\n Moves till now: {moves}')

        # it returns the moves in backtracking order 
        # so reverse it 
        
        moves.reverse()
        return moves
    
    # mapping of parent nodes, and the frontier with new configurations
    parent, frontier = {B: [None, None]}, [B]

    # We haven't found the middle point in which both explorations meet each other, so
    solved = False
    while not solved:
        # previous frontier as input to explore
        # so next frontier is created from last frontier
        # parent dict maps each config to its parent
        frontier = explore_frontier(frontier, parent)
        for node_config in frontier:            
            print('checking if solved or not')
            # breakpoint()
            # does this guarantees that in some cases will not explore the full graph ?
            # full graph is C(n, b, s) possible states 
            solved = check_solved(node_config, t)
            if solved:
                print('-------- SOLVED !!!')
                print(board_str(node_config))
                destination_config = node_config
                break

    # TODO 
    # should implement the C(n, b, s)
    # if the count reach the C(n, b, s) value and had not solved,
    # then return None

         
    M = unweighted_shortest_path(
        source_config=B,
        destination_config=destination_config,
        parent = parent
    )

    return M





####################################
# USE BUT DO NOT MODIFY CODE BELOW #
####################################
def move(B, d):
    '''
    Input:  B  | Board configuration
            d  | Direction: either 'up', down', 'left', or 'right'
    Output: B_ | New configuration made by tilting B in direction d
    '''
    n = len(B)
    B_ = list(list(row) for row in B)

    # Let us see a little about those moves
    
    if d == 'up':
        for x in range(n):  
            y_ = 0          
            for y in range(n):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ += 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'down':
        for x in range(n):  
            y_ = n - 1
            for y in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ -= 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'left':
        for y in range(n):  
            x_ = 0          
            for x in range(n):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ += 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    if d == 'right':
        for y in range(n):  
            x_ = n - 1
            for x in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ -= 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    B_ = tuple(tuple(row) for row in B_)
    return B_

def board_str(B):
    '''
    Input:  B | Board configuration
    Output: s | ASCII string representing configuration B
    '''
    n = len(B)
    rows = ['+' + ('-'*n) + '+']
    for row in B:
        rows.append('|' + ''.join(row) + '|')
    rows.append(rows[0])
    S = '\n'.join(rows)
    return S

def board_str_double(B1, B2, move):
    '''
    Input:  B1    | First board configuration
            B2    | Second board configuration
            move  | Move direction ('left', 'right', 'up', or 'down')
    Output: s     | ASCII string representing the transition from B1 to B2
    '''
    n = len(B1)
    rows = []

    # Determine the arrow symbol based on the move
    arrow_map = {'left': '<', 'right': '>', 'up': '^', 'down': 'v'}
    arrow = arrow_map.get(move, '?')

    # Creating the top and bottom borders
    border_row = '+' + ('-' * n) + '+' + '   ' + '+' + ('-' * n) + '+'
    rows.append(border_row)

    # Creating the rows with board elements and an arrow in between
    for row_B1, row_B2 in zip(B1, B2):
        row_str = '|' + ''.join(row_B1) + '|' + ' ' + arrow + ' ' + '|' + ''.join(row_B2) + '|'
        rows.append(row_str)

    rows.append(border_row)

    # Joining the rows to form the complete string
    return '\n'.join(rows)
