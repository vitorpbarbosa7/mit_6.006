


def prefix_max(A, i):

	if i > 0:
		# iteration using recurrence, moving pointer
		j = prefix_max(A, i - 1)
		if A[i] < A[j]:
			return j
	
	return i

def selection_sort(A, i = None):

	if i is None: i = len(A) - 1

	if i > 0:
		j = prefix_max(A, i)
		A[i], A[j] = A[j], A[i]
		selection_sort(A, i - 1)

if __name__ == '__main__':

	A = [8, 2, 4, 9, 3]

	selection_sort(A)

	print(A)
	
