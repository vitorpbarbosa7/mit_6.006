def merge_sort(A, a = 0, b = None):
	print('Stack frame created')

	if b is None:
		b = len(A)
	
	# a, b and c will change in each level
	c = (a + b + 1)//2

	# this is the return condition to do not enter into a new level of recursion (create new stack frame)	
	# if b - a is not greater than 1, therefore when calculating the middle, resulted in 0
	print(f'Length condition: a: {a}, b: {b}--> b - a: {b-a}')
	if b - a > 1:
		# Divide --------------
		# left node
		merge_sort(A, a, c)
		# right node
		merge_sort(A, c, b)

		# Conquer ---------------
		# auxiliar temporary arrays necessary for this implementation of mergesort
		# not in place
		L = A[a:c]
		R = A[c:b]
		
		print('\n---')
		print('A: ', A)
		print('L:', L)
		print('R: ', R)
		print('a: ', a)
		print('b: ', b)
		print('\n---')
	
		# merge part with the temporary storage L and R
		
		# a pointer is the beginning of left for each L and R
		# because they are separated from A, this works 
		# if not I would have to be together with relative incides on A 
		i, j = 0, 0
		
		while a < b:
			
			# dump left
			# 1st conditions 

			# 2nd condition
			# 	# 1st portion

			# . # 2nd portion
				# if left element is greater than right element
				# then we must put the left into the right portion 
				# the a index is this right portion ? 
			
			# this is the correct, it is the ok 
			# that is why we put in the first position the left one (because is small)
			if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
				print('R > L')
				# we put into the original array the element from left in this case
				A[a] = L[i]
				# therefore we can walk in left
				i += 1

			# this is the case in which is incorrect, when L is smaller than R 
			# therefore we put in the a position, the R
			else:
				print('L > R')
				# in this case we put into A the element from R
				A[a] = R[j]
				# and walk in R
				j += 1


			# A is receiving each element, therefore we walk in A also here, globally	
			a += 1
			print('A after', A)
			breakpoint()
		

A = [8,3,6,1,9,2,7,4]

merge_sort(A)
	
