
L = [1,2,3,4,5]

s = 0
for i in range(len(L)):
    s += L[i]
print(s)

def summation(i):
    print('stack frame created')
    # Base case:
    # like initialization in a looping
    if i > len(L)-1:
        return 0

    # what it calculates in this level of the stack?
    current_stack_value =  L[i]
    
    # how to connect what it is in this level of the stack to what is comming from a deeper level?
    # thinking about looping, that is when we will use the topological order
    next_level_stack = summation(i+1)

    # The relation itself
    # so this level of the stack will return the calculation from what it done from this level and the next
    result = current_stack_value + next_level_stack
    print(result)

    return result

# Original problem 
# We are now working with prefixes or suffixes?
summation(0)
