




B1 = [(2,2,3), (1, 3, 4)]
B2 = [(1,0,4)]

def max_book(B):

    max = B[0][2]
    for i in range(1, len(B) - 1, 1):
        if B[i][2] > max:
            max = B[i][2]

    return max

def min_book(B):

    min = B[0][1]
    for i in range(1, len(B) - 1, 1):
        if B[i][2] < min:
            min = B[i][2]

    return min

min_B1 = min_book(B1)
min_B2 = min_book(B2)
max_B1 = max_book(B1)
max_B2 = max_book(B2)

_min = min_B1 if min_B1 < min_B2 else min_B2
_max = max_B1 if max_B1 < max_B2 else max_B2

# print(B1)
# print(B2)

B = [0]*(_max+1)

def fill_array(Bi):
    
    i = 0 
    for single in Bi:

        # print(single)
        start = single[1]
        end = single[2]
        rooms = single[0]

        # print(start)
        # print(end)
        for i in range(start, end):
            B[i] += rooms
        # print(B)
        i += 1


fill_array(B1)
fill_array(B2)
print(B)


Bf = []

helper_array = [x for x in range(0, len(B)+1)]
# print(helper_array)

start = helper_array[0]

i = 0
j = 0

start = B[j]
while i < len(helper_array):

    while B[j] == B[j+1]:
        i += 1
        j += 1 

    tup = (B[j+1], start, i+1)
    print(tup)

    i += 1
    j += 1


    

