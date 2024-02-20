
# thinking about a dynamic programming approach
# the subproblem here will always be a suffix which we will keep it sorted by 
# looking for greatest element outside the suffix, to put it there

A = [7,8,5,4,6,3]


for i in range(len(A)-1, 0, -1):

	# unsorted prefix
	print(f'unsorted: {A[:i]}')
	# sorted suffix
	print(f'sorted: {A[i:]}')

	j = i - 1

	while j > 0:
		# biggest element will be given by this k pointer
		k = j
		# traversing still takes O(n**2)
		if A[j-1] > A[j]:
		# update biggest element
			k = j-1
		j -= 1	

	# After found the greatest element withing the pointer k
	# swaps with the ith element, from the outer loop
	# so there is a outer to define the suffix which is sorted, going from the n-1, backwards
	# and there is a inner loop for finding biggest element
	A[i], A[k] = A[k], A[i]
	
	print('A :', A)





