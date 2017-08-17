from stack_array import Stack

def parChecker(string):
	stack = Stack()
	for i in range(len(string)):
		if string[i] == '(':
			stack.push(string[i])
		elif string[i] == ')':
			if stack.isEmpty():
				return False
			else:
				stack.pop()
	if stack.isEmpty():
		return True
	return False

print(parChecker('((str)'))