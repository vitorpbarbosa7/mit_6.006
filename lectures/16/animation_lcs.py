from visualiser.visualiser import Visualiser as vs

A = 'HIEROGLYPHOLOGY'
B = 'MICHAELANGELO'

A = 'HABIT'
B = 'THEIR'

memo = [[None]*len(B) for _ in range(len(A))]
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def x(i,j):
    print(f'\nStack frame called')
    print(f'A[i:]: {A[i:]}')
    print(f'B[i:]: {B[j:]}')
    # breakpoint()

    # Base Case:
    # to avoid the infinity recursion call
    # when looking at the array of string it has no more values
    if i > len(A) - 1:
        return 0, []
    if j > len(B) - 1:
        return 0, []
    
    # Memoization check
    # if we already calculated the value, that is, the longest subsequence up until that moment
    # than we do not need to recalculate it
    if memo[i][j] is not None:
        return memo[i][j]

    # subproblem
    # look at suffixes, so in the dag, it will go to end level by cutting as A[i:]
    # and go back in the DAG returning the decision of that suffix

    # Relation
    # Cases, brute force
    # What we are working with ?
    # If the letters are equal, them we can count that we found some letters to count as next ones used in the subsequence

    # If not equal, keep one of them and go to the other look for another equal 
    # as the idea of looping

    # We must find the maximum subsequence possible, so:
    if A[i] == B[j]:
        print(f'\nLetter: {A[i]}')
        print(f'i: {i}')
        print(f'j: {j}')
        length, subsequence = x(i+1, j +1)
        memo[i][j] = (1 + length, [A[i]] + subsequence)
        return memo[i][j]
    
    else:
        length1, subsequence1 = x(i+1, j)
        length2, subsequence2 = x(i, j + 1)

        # max statement here, return what is the maximum length
        if length1 > length2:
            memo[i][j] = (length1, subsequence1)
        else:
            memo[i][j] = (length2, subsequence2)
        
        return memo[i][j]


x(0,0)
vs.make_animation("longest_commom_subsequence.gif", delay=2)