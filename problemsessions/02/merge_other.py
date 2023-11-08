from numpy import array as arr

def merge(A, i, j, last_digit):
    temp = A.copy()
    print(f"merging {A[i:j]} and {A[j:last_digit+1]}")
    init_i = i
    j_limit = j
    internal_counter = init_i

    while i < j and j < last_digit:
        if temp[i] > temp[j]:
            A[internal_counter] = temp[j]
            j += 1
        else:
            A[internal_counter] = temp[i]
            i += 1
        internal_counter += 1

    while i < j_limit:
        A[internal_counter] = temp[i]
        internal_counter += 1
        i += 1

    while j < last_digit:
        A[internal_counter] = temp[j]
        internal_counter += 1
        j += 1

    print(f"Result of merging: {A[init_i:last_digit+1]}")
    return A

def mergesort(A, i=0, j=None):
    if j is None:
        j = len(A)
    last_digit = j - 1

    print(f"List: {A[i:last_digit+1]}")

    if j - i < 2:
        return A[i:last_digit+1]
    else:
        mid = (i + j) // 2
        j = mid

        left = mergesort(A, i=i, j=j)
        right = mergesort(A, i=mid, j=last_digit)

        return merge(A, i, j, last_digit)

if __name__ == '__main':
    A = [7, 8, 5, 4, 3, 2, 1, 9]
    print(mergesort(A))
