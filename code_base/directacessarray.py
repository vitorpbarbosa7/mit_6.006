class E:
    def __init__(self, key):
        self.key = key

class DirectAccessArray:
	def __init__(self, u):
		# O(u): Allocate space in O(u) linear with the size of the largest key
		self.A = [None] * (u + 1)

	def __repr__(self):
		return '[' + ', '.join(str(x.key) if x is not None else ' ' for x in self.A) + ']'
	
	def find(self, k):
		# O(1) As stored the key values in the index, and allocated that very much space, then acces in O(1)
		return self.A[k]		  

	def insert(self, x):
		# O(1) access the x.key in O(1) and put it there
		self.A[x.key] = x         

	def delete(self, k):
		# O(1) acess the A[k] in constant time and set it to None, but this memory location will continue there not available for other
		self.A[k] = None		  

	def find_next(self, k):
		# from the key k, till the end of the allocated array, return the next one (assuming is ordered) ???

		# O(u) can for example have two keys, 1 and 999, it will take full length to find next one
		for i in range(k, len(self.A)):
			if self.A[i] is not None:
				return self.A[i]

	# Considering is sorted, just find the last value which exists and is not None
	# O(u), too much keys to look, as in the exmaple of 1,2,888, and the 999 were first key but was deleted, the space continues there, so 999 was set to None
	def find_max(self):
		for i in range(len(self.A) -1, -1, -1):
			if self.A[i] is not None:	
				return self.A[i]

	def delete_max(self):
		for i in range(len(self.A) -1, -1, -1):
			# find the non None max value and set the index to None??? wouldn't be the value to None? and key continues the same or not?
			x = self.A[i]
			if x is not None:
				self.A[i] = None
				return x

if __name__ == '__main__':

	X = [2,32,56,43,78,99]
	elements = [E(x) for x in X]
	# max key we find in O(n)
	u = max([el.key for el in elements])
	DAA = DirectAccessArray(u)
	for item in elements:
		DAA.insert(item)
	print(DAA)
	

