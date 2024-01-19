
# NOT WORKING


def max_score(i, j):
    print('Stack frame created')
    print(f'''
        i: {i}
        j: {j}
        A[i:j]: {A[i:j]}
          ''')
    breakpoint()
    # Base cases:
    if i == j:
        # if there is no poin to be hit, no point possible
        print('# Base Case 0 reached')
        return 0
    
    if abs(j - i) == 1:
        # if there is only one pin, we may hit it or not
        # maybe not hitting it at this level is better than hitting
        # because in a upper level in the stack we can choose another pin to be hit
        # even if at this level it was zero point
        print('# Base Case single value reached')
        return max(A[i], 0)
    

    # Inductive step, to Divide and Conquer

    # Divide:
    m = (i + j) // 2

    # hitting both pins

    La = max_score(i, m)
    print(f'La: {La}')
    Ra = max_score(m + 2, j)
    print(f'Ra: {Ra}')
    both_pins_score = A[m]*A[m+1] + La + Ra

    # hitting only one pin 
    Lb = max_score(i, m + 1)
    Rb = max_score(m + 1, j)
    one_pin_score = Lb + Rb

    return max(both_pins_score, one_pin_score)


if __name__ == '__main__':

    # A = [-1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]
    A = [-1, 1, 2, -1]
    max_score(0, len(A))