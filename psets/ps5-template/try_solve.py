from solve_tilt import move, board_str, board_str_double

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
        breakpoint()
        current_config = list_single_node_backtrack[0]
        current_move = list_single_node_backtrack[1]

        moves.append(current_move)
        print(f'\n Moves till now: {moves}')

    # it returns the moves in backtracking order 
    # so reverse it 
    
    moves.reverse()
    return moves

if __name__ == '__main__':

    config = (
        ('#', '#', '.', '.', '.'),
        ('.', 'o', '#', '.', '.'),
        ('.', '.', 'o', '.', '.'),
        ('.', '.', '.', '.', '.'),
        ('#', '#', '#', '.', '.')
    )
    t = (4, 3)

    # mapping of parent nodes, and the frontier with new configurations
    parent, frontier = {config: [None, None]}, [config]

    # We haven't found the middle point in which both explorations meet each other, so
    solved = False
    while not solved:
        # previous frontier as input to explore
        # so next frontier is created from last frontier
        # parent dict maps each config to its parent
        frontier = explore_frontier(frontier, parent)
        for node_config in frontier:            
            print('checking if solved or not')
            breakpoint()
            solved = check_solved(node_config, t)
            if solved:
                print('-------- SOLVED !!!')
                print(board_str(node_config))
                destination_config = node_config
                break

         
    moves = unweighted_shortest_path(
        source_config=config,
        destination_config=destination_config,
        parent = parent
    )
    print(moves)