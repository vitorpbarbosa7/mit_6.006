def fib_efficient(n, d):
    # memoization
    # keep track of the previously calculated values of other fib(n)
    # using this dictionary d
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        # store the recent calculated after many as needed stack calls of the recusion
        d[n] = ans
        print(d)
        return ans
    
if __name__ == '__main__':
    # Base cases in the hash table
    d = {0:1, 1:1}
    n = 7
    fib_efficient(n, d)


