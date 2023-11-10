
B1 = [(1,0,4), (2,4,5),(1,5,6)]
B2 = [(2,2,3), (1,3,4), (2,6,6)]

def merge_bookings(B1, B2):

    if isinstance(B1[0][0], tuple):
        B1 = list(B1[0])
    if isinstance(B2[0][0], tuple):
        B2 = list(B2[0])

    print('\n Call merge bookings')
    print(B1)
    print(B2)
    print('\n')

    n1, n2, i1, i2 = len(B1), len(B2), 0, 0

    x = 0
    B = []

    while i1 + i2 < n1 + n2:
        
        # if still there are elements for each one
        if i1 < n1: k1, s1, t1 = B1[i1]
        if i2 < n2: k2, s2, t2 = B2[i2]

        if i2 == n2:
            #traversing with x pointing to the same with s
            k, s, x = k1, max(x, s1), t1
            i1  +=1
        
        elif i1 == n1:
            k, s, x = k2, max(x, s2), t2
            i2 += 1

        else:
            if x < min(s1, s2):
                x = min(s1, s2)

            # disjoint
            if t1 <= s2:
                k, s, x = k1, x, t1
                i1 += 1

            elif t2 <= s1:
                k, s, x = k2, x, t2
                i2 += 1

            # joint
            elif x < s2:
                k, s, x = k1, x, s2

            elif x < s1:
                k, s, x = k2, x, s1

            else:
                k, s, x = k1 + k2, x, min(t1, t2)

                # if finished any of them 
                if t1 == x: i1 += 1
                if t2 == x: i2 += 1
        
        B.append((k, s, x))

    B_ = [B[0]]

    for k, s, t in B[1:]:
        k_, s_, t_ = B_[-1]
        if (k == k_) and (t_ == s):
            B_.pop()
            s = s_
        B_.append((k,s,t))

    print(f'Merged Bookings return: {B_}')
    
    return B_


if __name__ == '__main__':
    B = merge_bookings(B1, B2)
    print('\n', B)



