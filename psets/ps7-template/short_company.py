from single_company_shortest_value import single_company_shortest_value

def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    c = C[0]

    hashtable = {key: [value, 0, []] for key, value in zip(C, P)}
    print(hashtable)

    for company_name, v in hashtable.items():
          input = v[0]
          print(input)
          print(n)
          print(k)
        #   breakpoint()
          max_length, subsequennce = single_company_shortest_value(input, n, k)
          hashtable[company_name] = [input, max_length, subsequennce]

    print(hashtable)
#     breakpoint()

    c = max(hashtable, key=lambda company: hashtable[company][1])
    S = hashtable[c][2]

    print('\n ---------- Final result:')
    print(c)
    print(S)

    return (c, S)


if __name__ == '__main__':
        # cpnk = (
        #     ('SRTBOT', 'Try to Relax Inc.'),
        #     (
        #         (13, 25, 14, 2, 9, 17, 16, 13, 10, 16),
        #         (12, 19, 7, 17, 5, 10, 5, 25, 4, 20),
        #     ),
        #     5,
        #     2,
        # )
        
        short_company(*cpnk)
        