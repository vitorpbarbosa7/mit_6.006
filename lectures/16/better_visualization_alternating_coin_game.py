
from visualiser.visualiser import Visualiser as vs

A = [5,10,100,25]


@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def x(i, j, p):
    '''
    i: left end of the subtsring
    j: right end of the substring
    p: player of each time
    '''
    print('Stack frame created')
    substring = A[(i):(j+1)]
    print(f'Substring: {substring}')
    print(f'{i}-{j}')
    print(f'player: {p}')
    # breakpoint()

    # If substring reaches the single coin, as it will in the deeper levels of the recursion call:
    if i == j:
        if p == 'me':
            print('passei aqui')
            return A[i], A[i]
        else:
            # don't be confused, A[i] is here only for visualization purposes
            return A[i], 0
 
    if p == 'me':
        my_points_first = A[i]
        my_points_last = A[j]
        _, result_first = x(i+1, j, 'you')
        _, result_last = x(i, j-1, 'you')
        choose_first = my_points_first + result_first
        choose_last = my_points_last + result_last
        result = max(choose_first, choose_last)

    if p == 'you':
        my_points_you_first = 0
        my_points_you_last = 0
        _, result_first = x(i+1, j, 'me')
        _, result_last = x(i, j-1, 'me')
        choose_first = my_points_you_first + result_first
        choose_last = my_points_you_last + result_last
        # if the program is solving my strategy, we put a min here, because I want the sequence of events which will mininize your score and maximize mine
        result = min(choose_first, choose_last)

    return substring, result


# Original Problem:
n = len(A)

x(0, n-1, 'me')
vs.make_animation("better_visualization_alternating_coin_game.gif", delay=2)

_, result = x(0, n-1, 'me')
print(result)