''''
THIS ATTEMPTED SOLUTION DID NOT WORKED
'''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime_after(i):
    candidate = i + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

def _hash(x, a, b, p, m):

    return ((a*x + b) % p ) % m


if __name__ == '__main__':

    A = [47,61,36,52,56,33,92]

    # O(n)
    u = max(A)
    p = next_prime_after(u)
    print(p)

    hash_map = [_hash(x, a = 10, b = 4, p = p, m = len(A)) for x in A]    
    print(hash_map)