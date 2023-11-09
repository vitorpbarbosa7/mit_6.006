def find_datum_location(n, k):
    left, right = 1, n
    j = 0

    while left <= right:
        midpoint = (left + right) // 2

        if midpoint == k:
            return midpoint
        elif midpoint < k:
            left = 2 ** (j + 1)
        else:
            right = n - 2 ** (j + 1)
        j += 1
        print(f'left and right {left} - {right}')

    low, high = 2 ** (j - 1), 2 ** j

    while low <= high:
        midpoint = (low + high) // 2

        print(midpoint)

        if midpoint == k:
            return midpoint
        elif midpoint < k:
            low = midpoint + 1
        else:
            high = midpoint - 1

    return None

n = 10000
k = 9999
result = find_datum_location(n, k)
if result is not None:
    print(f"Πcard found Datum at kilometer {result}")
else:
    print("Datum not found.")

