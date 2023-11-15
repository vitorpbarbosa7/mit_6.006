
A = [47,61,36,52,56,33,92]


def _hash(x, a, b, p, m):

    return ((a*x + b) % p ) % m

# By the pigeonhole principle, 7 will result in collision, since 7 is the outermost value in the mod division

n = len(A)
for p in range(7,10000):
    hashmap = {}
    for x in A:
        h = _hash(x, a = 10, b = 4, p = p, m = n)
        if h in hashmap:
            next
        else:
            hashmap[h] = x

    if len(hashmap) == n:
        print('found ', p)
        break
