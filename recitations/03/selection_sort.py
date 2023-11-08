


A = [7,8,5,4,6,3]


for i in range(len(A)-1, 0, -1):

	print(f'unsorted: {A[:i]}')
	print(f'sorted: {A[i:]}')

	j = i - 1

	while j > 0:
		k = j
		# traversing still takes O(n**2)
		if A[j-1] > A[j]:
		# update biggest element
			k = j-1
		j -= 1	

	# ele encontra o maior elemento, e soh realiza a operacao de set ao final	
	A[i], A[k] = A[k], A[i]
	
	print('A :', A)





