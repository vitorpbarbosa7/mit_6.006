from solve_tilt import move, board_str, board_str_double

def neighbors(config):
    MOVES = ['up','down','left','right']
    ns = []
    for m in MOVES:
        new_config = move(config, m)
        # print(f'\n New neighbor from move {m}:')
        # print(S)
        # print(board_str_double(config, new_config, m))
        # breakpoint()
        ns.append(new_config)

    return ns

def explore_frontier(frontier, parent):

    new_frontier = []
    # explore one frontier of configurations
    # creating other frontier with new configurations
    for config in frontier:
        for new_config in neighbors(config):
            if new_config not in parent:
                parent[config] = config
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

def unweighted_shortest_path(source_config, destination_config, parent):

    initial_config = destination_config
    path = [destination_config]

    # go backtracking


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
    parent, frontier = {config: None}, [config]

    # We haven't found the middle point in which both explorations meet each other, so
    solved = False
    while not solved:
        # previous frontier as input to explore
        # so next frontier is created from last frontier
        # parent dict maps each config to its parent
        frontier = explore_frontier(frontier, parent)
        for config in frontier:            
            print('checking if solved or not')
            breakpoint()
            solved = check_solved(config, t)
            if solved:
                print('-------- SOLVED !!!')
                print(board_str(config))
                break

