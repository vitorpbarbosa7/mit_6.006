memo_size = {}
def cut_rod(l, v):

    # Base cases:
    if l < 1:
        # nothing to sell 
        return 0
    # if not in memo 
    if l not in memo_size:

        # Brute force all possibilities of cuts
        for p in range(1, l+1):
            x_ = v[p] + cut_rod(l-p, v)
            # check if the new calculated value for l, with some p, is greater than the already
            # stored in the memo for that l
            if (l not in memo_size) or (memo_size[l] < x_):
                memo_size[l] = x_

    return memo_size[l]
            

# Example Usage
L = 7
v= [0, 1, 10, 13, 18, 20, 31, 32]

max_value_seeling = cut_rod(L, v)
print(memo_size)
print(max_value_seeling)
