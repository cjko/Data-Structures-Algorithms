# Stacks using array implementation

class Stack(object):
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[len(self.stack)-1]

	def isEmpty(self):
		if self.stack:
			return False
		return True

	def size(self):
		return len(self.stack)
