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

        cpnk = (
            ('BitHub', 'GitBucket', 'GitBit'),
            (
                (33, 69, 91, 78, 19, 40, 13, 94, 10, 88, 43, 61, 72, 13, 46, 56, 41, 79, 82, 27, 71, 62, 57, 67, 34, 8, 71, 2, 12, 93),
                (52, 91, 86, 81, 1, 79, 64, 43, 32, 94, 42, 91, 9, 25, 73, 29, 31, 19, 70, 58, 12, 11, 41, 66, 63, 14, 39, 71, 38, 91),
                (16, 71, 43, 70, 27, 78, 71, 76, 37, 57, 12, 77, 50, 41, 74, 31, 38, 24, 25, 24, 5, 79, 85, 34, 61, 9, 12, 87, 97, 17),
            ),
            10,
            3,
        )
        
        short_company(*cpnk)
        