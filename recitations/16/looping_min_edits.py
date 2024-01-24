import numpy as np

def edit_distance(A, B):
    x = [[None]*len(B) for _ in range(len(A))]
    x[0][0] = 0

    for i in range(1, len(A)):
        x[i][0] = x[i-1][0] + 1
        print(np.matrix(x))
        breakpoint()
    for j in range(1, len(B)):
        x[0][j] = x[0][j-1] + 1
        print(np.matrix(x))
        breakpoint()


    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                x[i][j] = x[i-1][j-1]
            else:
                ed_del = 1 + x[i-1][j]
                ed_ins = 1 + x[i][j-1]
                ed_rep = 1 + x[i-1][j-1]
                x[i][j] = min(ed_del, ed_ins, ed_rep)
                print(np.matrix(x))
    return x[len(A) - 1][len(B) - 1]

A = 'BCDE'
B = 'FG'
result = edit_distance(A, B)
print(result)