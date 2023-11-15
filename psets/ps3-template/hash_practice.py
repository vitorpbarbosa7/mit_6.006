

A = [47,61,36,52,56,33,92]

def _hash(x, a, b, m):

    return (a*x + b) % m

hash_map = [_hash(x, a = 10, b = 4, m = len(A)) for x in A]    
print(hash_map)