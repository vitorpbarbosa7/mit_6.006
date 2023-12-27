# ----------------------------------- #
# REWRITE SOLVE IMPLEMENTING PART (e) # 
# ----------------------------------- #

 
def solve(config):

    def check(frontier, parent):
        # frontier of going from left to right with parent set of right to left
        # or 
        # frontier of going from right to left with parent set of left to right
        for f in frontier:
            if f in parent:
                return f
        return None
    parent_c, frontier_c = {config: None}, [config]
    parent_s, frontier_s = {SOLVED: None}, [SOLVED]

    # next level from going from left to right
    # and check if the parent set has this frontier
    middle = check(frontier_c, parent_s)

    while middle is None:
        frontier_c = explore_frontier(frontier_c, parent_c)
        # parent_c is reached by going in each loop iteration a level further, and stops when middle of left to right is equal to middle 
        # from right to left
        middle = check(frontier_c, parent_s)
        # termination condition, if the middle of both paths are found
        if middle: 
            break
        frontier_s = explore_frontier(frontier_s, parent_s)
        middle = check(frontier_s, parent_c)

    if middle:
        path_c = path_to_config(middle, parent_c)
        path_s = path_to_config(middle, parent_s)
        print(path_c)
        path_s.pop()
        path_s.reverse()
        return moves_from_path(path_c + path_s)
    
    return None

# --------------------------------------- #
# READ, BUT DO NOT MODIFY CODE BELOW HERE # 
# --------------------------------------- #
# Pocket Cube configurations are represented by length 24 strings
# Each character repesents the color of a small cube face
# Faces are laid out in reading order of a Latin cross unfolding of the cube

SOLVED = '000011223344112233445555'

def config_str(config):
    # Return config string representation as a Latin cross unfolding
    return """
             %s%s
             %s%s
           %s%s%s%s%s%s%s%s
           %s%s%s%s%s%s%s%s
             %s%s
             %s%s
           """ % tuple(config)

def shift(A, d, ps):
    # Circularly shift values at indices ps in list A by d positions
    values = [A[p] for p in ps]
    k = len(ps)
    for i in range(k):
        A[ps[i]] = values[(i - d) % k]

def rotate(config, face, sgn):
    # Returns new config by rotating input face of input config
    # Rotation is clockwise if sgn == 1, counterclockwise if sgn == -1
    assert face in (0, 1, 2)
    assert sgn in (-1, 1)
    if face is None:    return config
    new_config = list(config)
    if face == 0:
        shift(new_config, 1*sgn, [0,1,3,2])
        shift(new_config, 2*sgn, [11,10,9,8,7,6,5,4])
    elif face == 1:
        shift(new_config, 1*sgn, [4,5,13,12])
        shift(new_config, 2*sgn, [0,2,6,14,20,22,19,11])
    elif face == 2:
        shift(new_config, 1*sgn, [6,7,15,14])
        shift(new_config, 2*sgn, [2,3,8,16,21,20,13,5])
    return ''.join(new_config)

def neighbors(config):
    # Return neighbors of config
    ns = []

    # -- All allowed neighbors of a configuration, depending on what face is being rotated
    # and in which direction the rotation occurs
    for face in (0, 1, 2):
        for sgn in (-1, 1):
            ns.append(rotate(config, face, sgn))
    return ns

def explore_frontier(frontier, parent, verbose = False): 
    # Explore frontier, adding new configs to parent and new_frontier
    # Prints size of frontier if verbose is True
    if verbose:
        print('Exploring next frontier containing # configs: %s' % len(frontier))
    new_frontier = []
    for f in frontier:
        for config in neighbors(f):
            # as in breadth first search, if the vertex (configuration) does not exist
            # put it in the parent set, setting its key to its config and the value to its parent one, from which it came from 
            if config not in parent:
                parent[config] = f
                new_frontier.append(config)
    return new_frontier

def path_to_config(config, parent):
    # Given a set of configurations in a Tree of possibilities (graph of exploration), following each vertex one after the order
    # constructed using BFS
    # this function gets the full path, returning a linear one 

    # Return path of configurations from root of parent tree to config
    # path starts at final solved configuration, that is what is expected
    path = [config]
    while path[-1] is not None:
        # go back in the parent 
        path.append(parent[path[-1]])
    path.pop()
    path.reverse()
    return path

def moves_from_path(path):
    # Given path of configurations, return list of moves relating them
    # Returns None if any adjacent configs on path are not related by a move
    moves = []
    for i in range(1, len(path)):
        move = None
        for face in (0, 1, 2):
            for sgn in (-1, 1):
                if rotate(path[i - 1], face, sgn) == path[i]:
                    move = (face, sgn)
                    moves.append(move)
        if move is None:
            return None
    return moves

def path_from_moves(config, moves):
    # Return the path of configurations from input config applying input moves
    path = [config]
    for move in moves:
        face, sgn = move
        config = rotate(config, face, sgn)
        path.append(config)
    return path

def scramble(config, n):
    # Returns new configuration by appling n random moves to config
    from random import randint
    for _ in range(n):
        ns = neighbors(config)
        i = randint(0, 2)
        config = ns[i]
    return config

def check(config, moves, verbose = False):
    # Checks whether applying moves to config results in the solved config
    if verbose:
        print('Making %s moves from starting configuration:' % len(moves))
    path = path_from_moves(config, moves)
    if verbose:
        print(config_str(config))
    for i in range(1, len(path)):
        face, sgn = moves[i - 1]
        direction = 'clockwise'
        if sgn == -1:
            direction = 'counterclockwise'
        if verbose:
            print('Rotating face %s %s:' % (face, direction))
            print(config_str(path[i]))
    return path[-1] == SOLVED

def test(config):
    print('Solving configuration:')
    print(config_str(config))
    moves = solve(config)
    print(moves)
    if moves is None:   
        print('Path to solved state not found... :(')
        return
    print('Path to solved state found!')
    if check(config, moves):
        print('Move sequence terminated at solved state!')
    else:
        print('Move sequence did not terminate at solved state... :(')

if __name__ == '__main__':
    config = scramble(SOLVED, 100)
    test(config)
