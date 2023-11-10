
from solution import merge_bookings

# Steps:
# Make the splits
# Add the k = 1 , construct the tuple (1, s, t)

R = ((2, 19), (17, 18), (12, 25), (5, 15), (9, 11))

def mergesort(R):
    print(f'Stack frame created')

    # Base case, single Booking is already sorted
    if len(R) == 1:
        return (1, R[0][0], R[0][1])

    n = len(R)
    mid = n//2
    left = R[0:mid]
    right = R[mid:] 

    print(f'left before recursion: {left}')
    print(f'right before recursion: {right}')

    left = mergesort(left)
    right = mergesort(right)

    print(f'left after recursion: {left}')
    print(f'right after recursion: {right}')
    breakpoint()

    merged = merge_bookings([left], [right])
    

    return tuple(merged)


final = mergesort(R)

print(f'final is {final}')

