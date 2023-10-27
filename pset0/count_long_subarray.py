def count_long_subarray(A):
	'''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
	count = 0
    ##################
    # YOUR CODE HERE #
    ##################

	all_lengths = _check_sequence(A)

	if len(all_lengths) == 0:
		count = 0
	else:
		max_length = max(all_lengths)

		count = all_lengths.count(max_length)

	print(f'Number of max length subarrays: {count}')

	return count


def _check_sequence(A):
	
	all_sizes = []
	single_size = 0

	if len(A) == 0:
		return []

	init = 0
	for i in range(0, len(A)-1):
		#print('\n')
		#print(i)
		#print(f'A[i]: {A[i]}')
		#print(f'A[i+1]: {A[i+1]}')
		
		if A[i+1] > A[i]:
			subarray = A[init:i+2]
			#print(f'Updated subarray: {subarray}')
			single_size = len(subarray)
			#print(f'Array size: {single_size}')
			all_sizes.append(single_size)
		else:
			#print(f'Finished another sequence')
			init = i+1
		
		#print(f'All subarrays existing lenghts: {all_sizes}')

	return all_sizes


def testcases():

	#subarrays = _check_sequence(A)
	count_long_subarray(start_case)
	count_long_subarray(A)
	count_long_subarray(zero_array)
	count_long_subarray(singleton_array)
	count_long_subarray(only_one_length)
	count_long_subarray(twotwo)
	


if __name__ == '__main__':

	start_case = (7,8,9,4,5,6,1,2,3)
	A = (1,3,4,2,7,5,6,9,8) 
	
	zero_array = ()
	singleton_array = (7,)
	only_one_length = (9,8,7,6,5,4,3,2,1)
	twotwo = (8,9,6,7,4,5,2,3,0,1)
	
	#_check_sequence(singleton_array)	
	testcases()
	'''Desired output:
	- 3
	- 2
	- 0
	- 1
	- 9
	'''
