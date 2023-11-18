ORD_A = ord('a')

def lower_ord(c):
    return ord(c) - ORD_A

def count_anagram_substrings(T, S):

    m, n, k = len(T), len(S), len(S[0])

    D = {}                                      # map from freq tables to ocurrences
    F = [0] * 26                               # initial frequency table

    # traverse the full string
    for i in range(m):

        # add character to frequency table count
        F[lower_ord(T[i])] += 1

        # if i is already bigger them first word
        if i > k - 1:
            F[lower_ord(T[i - k])] -= 1

        if i >= k - 1:
            key = tuple(F)
            if key in D:
                D[key] += 1
            else:
                D[key] = 1

