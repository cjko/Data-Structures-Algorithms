class Queue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return str(self.queue)

	def enqueue(self, item):
		self.queue.append(item)
	
	def dequeue(self):
		item = self.queue[0]
		for i in range(len(self.queue)-1):
			self.queue[i] = self.queue[i+1]
		self.queue.pop()
		return item

	def isEmpty(self):
		if self.queue:
			return False
		return True

	def size(self):
		return len(self.queue)

class BST(object):
	def __init__(self):
		self.root = None

	def __str__(self):
		string = ''
		q = Queue()
		if self.root:
			q.enqueue(self.root)
		else:
			return None
		while not q.isEmpty():
			item = q.dequeue()
			string += ' %d ' % item.val
			if item.left:
				q.enqueue(item.left)
			if item.right:
				q.enqueue(item.right)
		return string

	def add(self, val):
		if not self.root:
			self.root = BSTNode(val)
		else:
			if val < self.root.val:
				if self.root.left:
					return self.root.left.add(val)
				else:
					self.root.left = BSTNode(val)
			elif val > self.root.val:
				if self.root.right:
					return self.root.right.add(val)
				else:
					self.root.right = BSTNode(val)
			else:
				return



class BSTNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def add(self, val):
		if val < self.val:
			if self.left:
				return self.left.add(val)
			else:
				self.left = BSTNode(val)
		elif val > self.val:
			if self.right:
				return self.right.add(val)
			else:
				self.right = BSTNode(val)
		else:
			return

bst = BST()
bst.add(50)
bst.add(25)
bst.add(75)
print(bst)












