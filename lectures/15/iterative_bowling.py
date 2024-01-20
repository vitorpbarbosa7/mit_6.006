# bottom up

def bowl(A):
    B = {}
    # Base cases:
    # equivalent to the other recursive return at last level of stack frame of 
    # recursive calls

    # the topological order, if we think about the recursive code, which is easier
    # is n, n-1, n-2, ... 3, 2, 1, 0
    B[len(A)] = 0
    B[len(A) + 1] = 0
for i in reversed(range(len(A)-1)):
        print(f'i: {i}')
        skip_one = B[i+1]
        hit_one = A[i] + B[i + 1]
        hit_both = A[i]*A[i+1] + B[i + 2]
        B[i] = max(
            skip_one, 
            hit_one, 
            hit_both
        )

    return B[0], B

if __name__ == '__main__':

    # A = [-1, 1, 2, -1]
    A = [-1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]
    max_score, memo = bowl(A)
    print(max_score)
    print(memo)
