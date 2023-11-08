A = [1,2,3,4,1,2,3,5]

def _get_index_special(A):

	for i in range(len(A)):
		if A[i] > A[i+1]:
			return i

def count_damage(A):
	
	s = _get_index_special(A)
	j = s+1
	i = 0
	
	damage_array = [None]*len(A)
	damage = 1
	while i < s+1:
		print(f'i: {i}')
		print(f'j: {j}')

		print(f'A[i] and A[j] are: {A[i]} and {A[j]}')
		if A[i] > A[j]:
			damage += 1
			print(f'damage updated: {damage}')
			j += 1 
		else:
			damage_array[i] = damage
			i += 1
		
	damage_array[s+1:] = [1]*(len(A)-(s+1))

	return damage_array

print(count_damage(A))


	
