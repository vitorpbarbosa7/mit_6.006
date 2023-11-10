



# B1 = [(1,0,4), (2,4,5),(1,5,6)]
# B2 = [(2,5,6), (1,6,7), (2,8,9)]

B1 = [(1,0,4)]
B2 = [(2,5,6)]

i1, i2 = 0, 0

k1, s1, t1 = B1[0]
k2, s2, t2 = B2[0]

# start

if s1 < s2:
    x = s1
    kx, sx, tx = B1[i1]
    ky, sy, ty = B2[i2]
else:
    x = s2
    kx, sx, tx = B2[i2]
    ky, sy, ty = B1[i2]

B = []
while i1 < len(B1) and i2 < len(B2):

    # Case 1 : next booking with no intersection with x

    if 



