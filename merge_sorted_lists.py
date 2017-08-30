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

def merge(listOne, listTwo):
	# mergedList = SLL()

	head = tail = ListNode(None)
	runnerOne = listOne.head
	runnerTwo = listTwo.head
	
	while runnerOne and runnerTwo:

		if runnerOne.val < runnerTwo.val:
			tail.next = runnerOne
			runnerOne = runnerOne.next
		else:
			tail.next = runnerTwo
			runnerTwo = runnerTwo.next
		tail = tail.next

	tail.next = runnerOne or runnerTwo
	return head.next


x = SLL()
x.head = ListNode(2)
x.head.next = ListNode(5)
x.head.next.next = ListNode(7)
y = SLL()
y.head = ListNode(3)
y.head.next = ListNode(11)
y.head.next.next = ListNode(18)
print(x)
print(y)
print(merge(x,y))

