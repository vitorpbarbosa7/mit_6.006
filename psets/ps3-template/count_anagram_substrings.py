def count_anagram_substrings(T, S):
        '''
        Input:  T | String
                S | Tuple of strings S_i of equal length k < |T|
        Output: A | Tuple of integers a_i:
                | the anagram substring count of S_i in T
        '''
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        n = len(T)
        Binit = S[0]
        print(Binit)
        print('\n')
        k = len(S[0])
        print(k)
        print('\n')
        # breakpoint()

        # get all letters in a dict
        characters = {key: 0 for key in ALPHABET}

        DAA = {}
        # traverse with k and construct the base 26 base frequency table

        for i in range(k):
                ch = T[i]
                characters[ch] += 1

        # this does not run in O(n) because we have a fixed amount of letters in the ascii lower case english ALPHABET (26)
        # so this is constant time
        mykey = int(''.join(map(str, characters.values())))     
        DAA[mykey] = 1

        for i in range(k, n):

                start_pointer = i-k
                end_pointer = i
                leftover_ch = T[start_pointer]

                # decrease the letter to the left
                characters[leftover_ch] -= 1

                new_ch = T[end_pointer]

                characters[new_ch] += 1

                # this does not run in O(n) because we have a fixed amount of letters in the ascii lower case english ALPHABET (26)
                # so this is constant time

                # now, how to implement this, without this string contatenation?
                
                mykey = int(''.join(map(str, characters.values())))
                if mykey not in DAA:
                        DAA[mykey] = 1
                else:
                        DAA[mykey] += 1

        print(DAA)
        print('\n')
        # breakpoint()

        def count(DAA, B):

                characters = {key: 0 for key in ALPHABET}

                for i in range(k):
                        ch = B[i]
                        characters[ch] += 1

                Bkey = int(''.join(map(str, characters.values())))

                if Bkey in DAA:
                        return DAA[Bkey]
                else:
                        return

        A = []
        for B in S:
                A.append(count(DAA, B))        
                print(A)
                print('\n')
                # breakpoint()

        return tuple(A)


if __name__ == '__main__':
        
        
        Ts = [
        'esleastealaslatet',
        'lrldrrrllddrrlllrddd', 
        'kkkkkvvuvkvkkkvuuvkuukkuvvkukkvkkvuvukuk', 
        'trhtrthtrthhhrtthrtrhhhtrrrhhrthrrrttrrttrthhrrrrtrtthhhhrrrtrtthrttthrthhthrhrh',
        'hjjijjhhhihhjjhjjhijjihjjihijiiihhihjjjihjjiijjijjhhjijjiijhjihiijjiiiijhihihhiihhiiihhiijhhhiijhijj'
        ]

        Ss = [
        ('tesla',),
        ('ldl', 'rld'),
        ('vkuk', 'uvku', 'kukk'),
        ('rrrht', 'tttrr', 'rttrr', 'rhrrr'),
        ('jihjhj', 'hhjiii', 'ihjhhh', 'jjjiji'),
        ]
        
        all_results = []
        for i in range(len(Ts)):
                T = Ts[i]
                S = Ss[i]

                print(T)
                print(S)
                print('\n')
                # breakpoint()

                A = count_anagram_substrings(T, S)
                all_results.append(A)


        print(all_results)
                