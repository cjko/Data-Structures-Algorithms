class SLL(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def __str__(self):
		string = ''
		current = self.head
		while current:
			string += str(current.val) + '->'
			current = current.next
		string += 'None'
		return string

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
	def __str__(self):
		string = ''
		current = self
		while current:
			string += str(current.val) + '->'
			current = current.next
		string += 'None'
		return string

def reverseSLL(sll):
	current = sll.head
	prev = None
	while current:
		next = current.next
		current.next = prev
		prev = current
		current = next
	sll.head = prev
	return sll

x = SLL()
x.head = ListNode(2)
x.head.next = ListNode(5)
x.head.next.next = ListNode(7)
print(reverseSLL(x))
print(x)