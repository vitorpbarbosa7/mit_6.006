# Only finally understood the solution, tried hard but could not solve

# the thing was to realize considering always two consecutive days and forcing a item to be in the sequence
# (like in the LIS), we get to form a longest decreasing subsequence, breaking when no item in a day is added 

def short_company(C, P, n, k):
    S = []
    for i in range(len(C)):
        p = P[i]
        memo = [None for _ in range(n*k)]
        
        def dp(j):
            if memo[j] is None:
                #j = current item which will be included in the subsquence
                # (k-1) - (j mod k) - items remaining in the same day
                # k consider next day 

                # this way we are considering always two consecutive days to have items 
                # if they do not have items, the subsequencer will broke and start another one 
                f = min(j + (k-1) - (j % k) + k, n*k - 1)
                x, r = 1, None

                # considering from current item and items till next day
                # here we return the number of items in the subsequence 
                for d in range(j+1, f+1):
                    x_, _ = dp(d)

                    # price before must be higher than a later price
                    if (p[j] > p[d]) and (1 + x_ > x):
                        x, r = 1 + x_ , d
                
                memo[j] = (x, r)

            return memo[j]
        
        best, opt = 0, 0
        for j in range(n*k):
            x, _ = dp(j)
            if x > opt:
                best, opt = j, x 

        if opt > len(S):
            c, S = C[i], []

            while best != None:
                S.append(p[best])
                _, best = dp(best)
        
    S = tuple(S)
    return (c, S)