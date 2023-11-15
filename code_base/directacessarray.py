
class DirectAccessArray:
	def __init__(self, u):
		self.A = [None] * u       # O(u): Allocate space in O(u) linear with the size of the largest key
	
	def find(self, k):
		return self.A[k]		  # O(1) As stored the key values in the index, and allocated that very much space, then acces in O(1)

	def insert(self, x):
		self.A[x.key] = x         # O(1) access the x.key in O(1) and put it there

	def delete(self, k):
		self.A[k] = None		  # O(1) acess the A[k] in constant time and set it to None, but this memory location will continue there not available for other

	def find_next(self, k):
		# from the key k, till the end of the allocated array, return the next one (assuming is ordered) ???
		for i in range(k, len(self.A):				# O(u) can for example have two keys, 1 and 999, it will take full length to find next one
			if A[i] is not None:
				return A[i]

	# Considering is sorted, just find the last value which exists and is not None
	# O(u), too much keys to look, as in the exmaple of 1,2,888, and the 999 were first key but was deleted, the space continues there, so 999 was set to None
	def find_max(self):
		for i in range(len(self.A) -1, -1, -1):
			if A[i] is not None:	
				return A[i]

	def delete_max(self):
		for i in range(len(self.A) -1, -1, -1):
			# find the non None max value and set the index to None??? wouldn't be the value to None? and key continues the same or not?
			x = A[i]
			if x is not None:
				A[i] = None
				return x

# TODO 
# testing cases