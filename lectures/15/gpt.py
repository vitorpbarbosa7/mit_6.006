def max_score(A):
    n = len(A)

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return max(A[0], 0)
    
    # Divide
    m = n // 2

    # Conquer
    # Case 1: Hit both pins m and m + 1 together
    score_both = A[m] * A[m + 1]
    if m + 2 < n:
        score_both += max_score(A[m + 2:])

    # Case 2: Don't hit both pins together
    score_single = max_score(A[:m + 1]) + max_score(A[m + 1:])

    # Combine
    return max(score_both, score_single)

if __name__ == '__main__':
    # Example usage
    A = [-1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]
    result = max_score(A)
    print(f'Maximum score: {result}')
