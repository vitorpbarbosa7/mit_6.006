def count_anagram_substrings(T, S):
        '''
        Input:  T | String
                S | Tuple of strings S_i of equal length k < |T|
        Output: A | Tuple of integers a_i:
                | the anagram substring count of S_i in T
        '''
        n = len(T)
        Binit = S[0]
        print(Binit)
        print('\n')
        k = len(S[0])
        print(k)
        print('\n')
        # breakpoint()

        ORD_A = ord('a')
        def lower_ord(c):
                return ord(c) - ORD_A

        # get all letters in a dict
        characters = [0]*26

        DAA = {}
        # traverse with k and construct the base 26 base frequency table

        for i in range(k):
                ch = T[i]
                ch_position = lower_ord(ch)
                characters[ch_position] += 1

        # this does not run in O(n) because we have a fixed amount of letters in the ascii lower case english ALPHABET (26)
        # so this is constant time

        # tuples are hashable
        # page 82 from "Introduction to computation and programming using python - mit press"
        mykey = tuple(characters)
        DAA[mykey] = 1

        for i in range(k, n):

                start_pointer = i-k
                end_pointer = i
                leftover_ch = T[start_pointer]

                # decrease the letter to the left
                ch_position = lower_ord(leftover_ch)
                characters[ch_position] -= 1

                # increase new ocurrence, sliding right
                new_ch = T[end_pointer]
                ch_position = lower_ord(new_ch)
                characters[ch_position] += 1
                
                mykey = tuple(characters)
                if mykey not in DAA:
                        DAA[mykey] = 1
                else:
                        DAA[mykey] += 1

        print(DAA)
        print('\n')
        # breakpoint()

        def count(DAA, B):

                characters = [0]*26

                for i in range(k):
                        ch = B[i]
                        ch_position = lower_ord(ch)
                        characters[ch_position] += 1

                Bkey = tuple(characters)

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
                