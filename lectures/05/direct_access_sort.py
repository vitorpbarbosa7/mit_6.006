

def direct_access_sort(A):

	#O(n) find maximum value 
	u = 1 + max(A) 

	#O(u) direct access array initialization (u >> n is a possibility)
	DAA = [None] * u 

	#O(n) -  Put all values of x in the new DAA as keys, so that to reach them we will access in constant time
	for x in A:    
		DAA[x] = x

	# O(u) - Reorganize, inplace the keys in the original array, 
	i = 0   
	j = 0
	while j < len(DAA):  
		if DAA[j] is not None:
			A[i] = DAA[j]
			i += 1
		j += 1

	return A


A = [1,3,4,2,8,5,9]
Asorted = sorted(A)
print(Asorted)


# is not able to sort arrays with repeated keys, because it will eliminate the key 
# we could use another data structure as chain ?
Asol = direct_access_sort(A)
print(Asol)
assert Asol == Asorted
	
