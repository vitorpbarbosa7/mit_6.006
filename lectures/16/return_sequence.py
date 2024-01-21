A = 'HABIT'
B = 'THEIR'

memo = [[None]*len(B) for _ in range(len(A))]
def x(i, j):
    print(f'\nStack frame called')
    print(f'A[i:]: {A[i:]}')
    print(f'B[i:]: {B[j:]}')

    # Base Case:
    if i > len(A) - 1 or j > len(B) - 1:
        return 0, []

    # Memoization check
    if memo[i][j] is not None:
        return memo[i][j]

    # Relation
    if A[i] == B[j]:
        print(f'\nLetter: {A[i]}')
        print(f'i: {i}')
        print(f'j: {j}')
        length, subsequence = x(i+1, j+1)
        memo[i][j] = (1 + length, [A[i]] + subsequence)
        return memo[i][j]
    
    else:
        length1, subsequence1 = x(i + 1, j)
        length2, subsequence2 = x(i, j + 1)

        if length1 > length2:
            memo[i][j] = (length1, subsequence1)
        else:
            memo[i][j] = (length2, subsequence2)

        return memo[i][j]

length, subsequence = x(0, 0)
print(f'Length of the longest subsequence: {length}')
print(f'Longest subsequence: {" ".join(subsequence)}')