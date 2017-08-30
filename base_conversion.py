# How to convert to a base:
# 1. Divide the decimal by the base until there is nothing left to divide
# 2. Keep track of how many remainders you have each time you divide
# 3. An array of those remainders is your decimal number in the new base (right to left)


def baseConversion(num, base):
	digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	if num == 0:
		return []
	quotient = num // base
	remainder = num % base
	return baseConversion(quotient, base) + [digits[remainder]]

print(''.join(baseConversion(12341323423,16)))