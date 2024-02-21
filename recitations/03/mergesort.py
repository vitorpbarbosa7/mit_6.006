def merge_sort(A, a = 0, b = None):
	print('Stack frame created')

	if b is None:
		b = len(A)
	
	# a, b and c will change in each level
	c = (a + b + 1)//2
	
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
		print(A)
		print(L)
		print(R)
		print(a)
		print(b)
		print('\n---')
	
		# merge part with the temporary storage L and R
		
		# a pointer is the beginning of left
		i, j = 0, 0
		
		while a < b:
			
			# dump left
			if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
				A[a] = L[i]
				i += 1

			# dump right
			else:
				A[a] = R[j]
				j += 1
	
			a += 1
			print('A after', A)
			breakpoint()
		

A = [8,3,6,1,9,2,7,4]

merge_sort(A)
	
