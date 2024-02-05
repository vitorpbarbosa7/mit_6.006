# from visualiser.visualiser import Visualiser as vs

A = [3,4,3,1]
memo = []
# @vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def x(i, t):
    print('Stack frame called')
    print(f'{A[i:]}')
    # breakpoint()

    # Base case
    # nothing to make up for the t
    n = len(A)
    if (i == n) and (t==0):
        return True
    if (i == n) and (t!=0):
        return False

    # brute force options 
    # THE KEY POINT IS IN THE t - A[i]
    # IF SEQUENTIALLY THE t - A[i] count is made, it means the A[i] were chosen
    use_ai = x(i+1, t - A[i])
    dont_use_ai = x(i+1, t)

    result = any(
        [use_ai,
        dont_use_ai]
    )

    if use_ai is True:
        memo.append(A[i])

    return result

T = 6
result = x(0, T)
# vs.make_animation("lis_subsetsum.gif", delay=2)
print(result)
