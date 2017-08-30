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

def checkCycle(sll):
	slow = sll.head
	fast = sll.head
	while slow:
		slow = slow.next
		fast = fast.next.next
		if fast == slow:
			return True
	return False

sll = SLL()
sll.head = ListNode(1)
x = ListNode(2)
sll.head.next = x
sll.head.next.next = ListNode(3)
sll.head.next.next.next = ListNode(4)
sll.head.next.next.next.next = x

print(checkCycle(sll))