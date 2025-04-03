A = 'CARBOHYDRATE'

memo = {}
n = len(A)

def LIS(i):
    # Base case: if we've reached the end, length is 0.
    if i == n:
        return (0, [])

    # If already solved, use memo
    if i in memo:
        return memo[i]

    # Include A[i] itself
    max_length = 1
    subsequence = [A[i]]

    # Check all possible next elements
    for j in range(i + 1, n):
        # only for those which are allowed
        if A[j] > A[i]:
            # return the full length from subprobem, and also the full subsequence (not only one letter)
            j_length, j_subseq = LIS(j)
            # we add the current one, if it makes bigger than the max_length from current recurrence level
            if 1 + j_length > max_length:
                # update max_length, that is basically the length with current letter
                max_length = 1 + j_length
                # add letter to the subsequence
                subsequence = [A[i]] + j_subseq

    # return length and subssequence up till now
    memo[i] = (max_length, subsequence)
    return memo[i]

def find_LIS():
    max_overall = 0
    best_subsequence = []

    # Try all starting points,  0 =< i =< |A|
    for i in range(n):
        length, subsequence = LIS(i)
        # if next length (starting from another point, is bigger, therefore use it)
        if length > max_overall:
            max_overall = length
            best_subsequence = subsequence

    return max_overall, best_subsequence

length, subsequence = find_LIS()
print("Length:", length)
print("Subsequence:", ''.join(subsequence))