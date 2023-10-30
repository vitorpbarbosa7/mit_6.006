

class StaticArray:

	def __init__(self, n):
		self.data = [None] * n 

	def get_at(self, i):
		if not ( 0 <= i < len(self.data)): raise IndexError
		return self.data[i]

	def set_at(self, i, x):
		if not (0 <= i < len(self.data)): raise IndexError
		self.data[i] = x

def birthday_match(students):
	
	#-- get length of a collection in python, possible list, O(1) constant time
	n = len(students)										
	
	#-- Allocation of memory in O(n)
	record = StaticArray(n)
	
	#-- n size loop
	for k in range(n):

		#-- Access any record in the collection students, will be possible in O(1) constant time
		# access each name and birthday of each student
		(name1, bday1) = students[k]
		
		#-- k size loop
		for i in range(k):
			
			#-- get any value in record, done in constant time O(1)
			# from out static array, returns a register
			(name2, bday2) = record.get_at(i)
			
			#-- Comparison contant time O(1)
			# if found two equals birtdays, stop
			if bday1 == bday2:
				return (name1, name2)
		
		#-- Set any value in constant time
		# if the code did not return any, none were equal
		# so after going through all k registers in the staticarray, and not founding any equal to the register in students, we 
		# set a new name into the staticarray
		record.set_at(k, (name1, bday1))

	# if not returned any before
	return None


