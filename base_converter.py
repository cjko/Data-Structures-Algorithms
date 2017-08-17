from stack_array import Stack

def baseConverter(decNumber, base):
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	remstack = Stack()

	while decNumber > 0:
		print('DEC Number %d'%decNumber)
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber // base

	newString = ""
	while not remstack.isEmpty():
		newString = newString + digits[remstack.pop()]
	
	return newString

print(baseConverter(26,26))