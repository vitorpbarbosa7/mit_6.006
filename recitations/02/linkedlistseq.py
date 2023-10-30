

class LinkedListNode:

	def __init__(self, X):
		self.item = X
		self.next = None
	
	# responsible for going each node at a time and stop when i = -, nice, very useful
	def later_node(self, i):
		if i == 0: return self
		assert self.next

		# print(f'Current: {self.item}')
		# the self.next structure guarantees he's walking through the linked list, so when reach i == 0 will be at the original we proposed
		return self.next.later_node(i-1)


class LinkedListSeq:

	# O(1)
	def __init__(self):
		self.head = None
		self.size = 0 

	# O(1)
	def __len__(self): return self.size

	# O(n)
	def __iter__(self):
		node = self.head
		while node:
			yield node.item
			node = node.next

	# O(n)
	def build(self, X):
		for a in reversed(X):
			self.insert_first(a)

	# O(i)
	def get_at(self, i):
		node = self.head.later_node(i)
		return node.item

	# O(i)
	def set_at(self, i, X):
		node = self.head.later_node(i)
		node.item = X

	# O(1)
	def insert_first(self, X):
		new_node = LinkedListNode(X)
		# new node at first point to the current head
		new_node.next = self.head
		# remap head to this first node
		self.head = new_node
		self.size += 1

	# O(1)
	def insert_at(self, i, X):
		if i == 0:
			self.insert_first(X)
			return
		new_node = LinkedListNode(X)
		node = self.head.later_node(i-1)
		new_node.next = node.next
		node.next = new_node
		self.size += 1

	# O(i)
	def delete_at(self, i):
		if i == 0:
			return self.detete_first()
		
		# return the previous one so that we can remap the pointer
		node = self.head.later_node(i-1)
		
		# the one which will be deleted		
		X = node.next.item

		node.next = node.next.next

		self.size -= 1

		# why bother returning? 
		return X

	def insert_last(self, X):	self.insert_at(len(self), X)
	def delete_last(self):	return self.delete_at(len(self) - 1)