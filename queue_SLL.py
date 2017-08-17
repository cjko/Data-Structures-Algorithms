class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class Queue(object):
	def __init__(self):
		self.head = None

	def __str__(self):
		string = ''
		runner = self.head
		while runner:
			string += str(runner.val) + ' -> '
			runner = runner.next
		string += 'None'
		return string

	def enqueue(self, item):
		if not self.head:
			self.head = ListNode(item)
		else:
			runner = self.head
			while runner.next:
				runner = runner.next
			runner.next = ListNode(item)

	def dequeue(self):
		if not self.head:
			return None
		elif self.head:
			item = self.head
			self.head = self.head.next
			return item

	def isEmpty(self):
		if not self.head:
			return True
		return False

	def size(self):
		count = 0
		runner = self.head
		while runner:
			count += 1
			runner = runner.next
		return count

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
print(q)
print(q.size())

