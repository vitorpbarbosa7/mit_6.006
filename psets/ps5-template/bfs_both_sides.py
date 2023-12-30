from solve_tilt import move, board_str, board_str_double

def neighbors(config):
    MOVES = ['up','down','left','right']
    ns = []
    for m in MOVES:
        new_config = move(config, m)
        # print(f'\n New neighbor from move {m}:')
        # print(S)
        # print(board_str_double(B, Bnext, m))
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

def _check_match(frontier, parent):
    '''
    Checks if the configurations in one of the frontiers already appears in the parent set 
    of configurations from the other side exploration
    If found that node, than this is the "middle", the point in which both explorations from 
    bfs, from both sides, meet each other, therefore we can construct the full path
    '''

    for config in frontier:
        if config in parent:
            return config
        
    return None

if __name__ == '__main__':

    config = (
        ('#', '#', '.', '.', '.'),
        ('.', 'o', '#', '.', '.'),
        ('.', '.', 'o', '.', '.'),
        ('.', '.', '.', '.', '.'),
        ('#', '#', '#', '.', '.')
    )

    # mapping of parent nodes, and the frontier with new configurations
    parent, frontier = {config: None}, [config]

    # We haven't found the middle point in which both explorations meet each other, so
    middle = None
    cont = 1
    while cont < 100:
        # previous frontier as input to explore
        # so next frontier is created from last frontier
        # parent dict maps each config to its parent
        frontier = explore_frontier(frontier, parent)
        print(len(parent))
        cont += 1
