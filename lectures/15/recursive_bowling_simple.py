# top down 
# think about the recursive calls 
# from top to the bottom

def bowl(A):
    memo = {}
    def B(i):
        print('Stack frame created')
        print(f'i: {i}')
        print(f'A: {A[i:]}\n')
        # Base case:
        # when in the recursive tree reached the last level it will return 0 points 
        # (no pin to be hit)
        if i >= len(A)-1:
            return 0 
        # if we have not calculated that from last to back suffix
        # So it will not go down into another recursive call if the memo has already stored the value for that specific prefix, suffix of substring
        if i not in memo:
            # go to another pin without counting this one
            skip_pin_score = B(i+1)
            # once in this level the pin is hit, we must go to another
            hit_pin = A[i] + B(i + 1)
            hit_both_pins = A[i]*A[i+1] + B(i + 2) 
            memo[i] = max(
                skip_pin_score,
                hit_pin,
                hit_both_pins
            )
        return memo[i] 
    return B(0), memo

if __name__ == '__main__':

    # A = [-1, 1, 2, -1]
    A = [-1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]
    max_score, memo = bowl(A)
    print(max_score)
    print(memo)