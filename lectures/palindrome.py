
def to_chars(s):
    '''pre processing'''
    s = s.lower()
    ans = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans = ans + c
    return ans


def isPal(s):
    '''
    Recursive function 
    '''
    print('----- Stack frame created ----')
    print(s)
    # Base case, no need to call recursion
    if len(s) <= 1:
        return True
    else:
        # Recursively call the middle part of the palindrome
        return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
    #preprocess
    s= to_chars(s)

    # Call the recursive function 
    result = isPal(s)

    return result

if __name__ == '__main__':
     
     s = 'are we not drawn onward, we few, drawn onward to new era'

     print(isPalindrome(s))

    
        
        