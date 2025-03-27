# Insertion Sort algorithm

A = [7,8,5,2,4,6,3]

# we must compare the A[i] with the A[i-1], if the right is less than the left, 
# then swap
# algorithm go by swaping adjacent values

# untill A[:i] is sorted
# sorted
#A[:i]

# the remaining is still unsorted  
# unsorted
#A[i:]

# count the number of swaps just for fun
swaps = 0
# consider the full length
# O(n) passes
for i in range(0, len(A) - 1):
    
    # know before hand where it should stop
	j = i
    
    # stop when reached the final part of the array
    # going from the start to the end
    # O(n) passes
    # while we still have not reached the limit of the array (inferior)
    # and still have for two elements at this point, they are reversed, continue the swaps
	while j > 0 and A[j-1] > A[j]:
		print(A)
		if A[j-1] > A[j]:
			A[j-1], A[j] = A[j], A[j-1]
			swaps +=1    
	
		j -= 1
	
	print(f'Sorted subarray: {A[:i]}')
	print(f'Unsorted subarray: {A[i:]}\n')

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
