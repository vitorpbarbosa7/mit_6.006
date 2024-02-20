def prefix_max(A, i):

	if i > 0:
		# iteration using recurrence, moving pointer
		# find biggest element from 0 to ith element, which makes sense to 
		# make the swap later
		j = prefix_max(A, i - 1)
		if A[j] > A[i]:
			return j

	# Base Case	
	return i

def selection_sort(A, i = None):

	if i is None: 
		i = len(A) - 1

	if i > 0:
		# find the prefix of the maximum element, to make the swap
		j = prefix_max(A, i)
		A[i], A[j] = A[j], A[i]
		# suffix subproblem of the dynamic program
		selection_sort(A, i - 1)

if __name__ == '__main__':

	A = [8, 2, 4, 9, 3]

	selection_sort(A)

	print(A)
	
