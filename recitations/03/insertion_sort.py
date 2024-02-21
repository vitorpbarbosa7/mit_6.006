

A = [7,8,5,2,4,6,3]

# we must compare the A[i] with the A[i-1], if the right is less than the left, 
# then swap
# algorithm go by swaping adjacent values

# sorted
#A[:i]

# unsorted
#A[i:]

swaps = 0
for i in range(0, len(A) - 1):
	
	j = len(A) - 1
	
	while j > i:
		print(A)
		# if the last element is the smallest, it will keep moving till the beginning of the array 
		# making the prefix as the subproblem which is sorted at the end of a single call in i
		if A[j-1] > A[j]:
			A[j-1], A[j] = A[j], A[j-1]
			swaps +=1    
	
		j -= 1
	
	print(f'Sorted subarray: {A[:i]}')
	print(f'Unsorted subarray: {A[i:]}')

print(swaps)

# swap is inside the inner loop, so makes O(n**2) set_at operations
# algorithm occurs inplace
# there are two loops, so the get_at operation occurs in O(n**2)


# A = [7,8,5,2,4,6,3]

# swaps = 0
# for i in range(1, len(A)):
	
# 	j = i
	
# 	# go out of the inner loop there is no swap to make anymore
# 	while j > 0 and A[j] < A[j-1]:
#  		print(A)
# 		A[j-1], A[j] = A[j], A[j-1]
	
# 		j -= 1
# 		swaps += 1
	
# 	print(f'Sorted subarray: {A[:i]}')
# 	print(f'Unsorted subarray: {A[i:]}')

# print(swaps)
