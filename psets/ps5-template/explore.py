from solve_tilt import move, board_str

def neighbors(B):
    MOVES = ['up','down','left','right']
    ns = []
    for m in MOVES:
        B = move(B, m)
        S = board_str(B)
        print(f'\n New neighbor from move {m}:')
        print(S)
        breakpoint()
        ns.append(S)

    return ns

def explore_frontier(frontier, parent):

    new_frontier = []
    for f in frontier:
        for config in neighbors(f):
            if config not in parent:
                parent[config] = f
                new_frontier.append(config)

    return new_frontier

if __name__ == '__main__':

    config = (
        ('#', '#', '.', '.', '.'),
        ('.', 'o', '#', '.', '.'),
        ('.', '.', 'o', '.', '.'),
        ('.', '.', '.', '.', '.'),
        ('#', '#', '#', '.', '.')
    )
    print(f'Initial configuration:\n')
    print(board_str(config))

    # mapping of parent nodes, and the frontier with new configurations
    parent, frontier = {config: None}, [config]

    explore_frontier(frontier, parent)