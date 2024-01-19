

def merge(L, R, A, i, j, a, b):

	'''
	L: Left portion
	R: Right portion
	A: original full array
	i: len(L)
	j: len(R)
	'''

	# Each call of the subproblem solves has work of n/2, it is smallest in deeper levels of the recursion tree
	# And it is higher in higher levels of the tree, since it will have to make the two finger algorithm for n numbers?
	
	print('\n------------ Merge Stack created -------------')
	print(f'''
	L: {L}
	R: {R}
	A: {A}
	i: {i}
	j: {j}
	a: {a}
	b: {b}
	''')
	breakpoint()

	if a < b:
		# if j equals zero, then all elements in right portion are already put into right place in A
		# or if still exists elements in left place and left is bigger then right
		# Put this left element at the last position in b
		if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
			A[b - 1] = L[i - 1]
			i -= 1
		else:
			# Put right element at last position in b
			A[b-1] = R[j - 1]
			j -= 1

		print(f'inplace reorder done: {A}')
		breakpoint()
		# Exactly decrease b, because b is the pointer to the last position, therefore, the previous b was already ordered, going level further to order the get the 
		# b - 1 position right
		merge(L, R, A, i, j, a, b - 1)

def merge_sort(A, a = 0, b = None):

	print(f'\nMergeSort Stack Frame created')
	print(f'a: {a}, b: {b}')
	print(f'Pointers define array: {A[a:b]}')
	breakpoint()

	if b is None: b = len(A)
		
	if b - a > 1:
		# get middle 
		c = (a + b + 1)//2
		
		# Left part, using the pointers and original inplace A full array
		merge_sort(A, a, c)
		# Right part, using the pointers and original inplace A full array
		merge_sort(A, c, b)
		
		# Resulting Left Part (new data was created, so why bother not returning?
		L = A[a:c]
		print(f'L array: {A[a:c]}')
		# Resulting Right Part (new data created)
		R = A[c:b]
		print(f'R array: {A[c:b]}')
	
		merge(L, R, A, len(L), len(R), a, b)


if __name__ == '__main__':

	A = [7,1,5,6,2,4,9,3]

	merge_sort(A)	
	
	print(f'Sorted A: {A}')

