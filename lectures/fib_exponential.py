
def fib(n):

    # Base case
    if n == 0 or n == 1:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)
    

if __name__ == '__main__':

    print(fib(0))
    print(fib(1))
    print(fib(7))