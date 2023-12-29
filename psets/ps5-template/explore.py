from solve_tilt import move, board_str, board_str_double

def neighbors(B):
    MOVES = ['up','down','left','right']
    ns = []
    for m in MOVES:
        Bnext = move(B, m)
        # print(f'\n New neighbor from move {m}:')
        # print(S)
        print(board_str_double(B, Bnext, m))
        breakpoint()
        ns.append(Bnext)

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

    # mapping of parent nodes, and the frontier with new configurations
    parent, frontier = {config: None}, [config]

    # deep explore with bfs, to get the intuition:
    cont = 1
    while cont < 100:
        frontier = explore_frontier(frontier, parent)
        print(len(parent))
        cont += 1
