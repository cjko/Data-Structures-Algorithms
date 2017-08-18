windowList = [188930, 194123, 201345, 210000, 220000, 180000, 230000]

'''
4+3+2+1
Increasing subranges:
increasing = false
188930 -> 194123

increasing = true
194123 -> 201345
because increasing is still true, we need to multiply i by 2
188930 -> 194123 -> 201345

increasing = true
201345 -> 210000
188930 -> 194123 -> 201345 ->210000
194123 -> 201345 -> 210000

increasing = true
210000 -> 220000
188930 -> 194123 -> 201345 ->210000 -> 2200000
194123 -> 201345 -> 210000 -> 2200000
201345 -> 210000 -> 2200000


Decreasing subranges:
201345 -> 154243

Non-change
154243 -> 154243

'''

def subranges(windowList):
	increasing = False
	decreasing = False
	totalIncreases = 0
	totalDecreases = 0
	increase = 0
	decrease = 0

	for i in range(len(windowList)):
		if i != 0:
			if windowList[i] > windowList[i-1]:
				if increasing:
					increase += 1
				else:
					increase = 1
				increasing = True
				decreasing = False
				totalIncreases += increase

			if windowList[i] < windowList[i-1]:
				if decreasing:
					decrease += 1
				else:
					decrease = 1
				increasing = False
				decreasing = True
				totalDecreases += decrease
		i += 1
	print('Increasing: %d' % totalIncreases)
	print('Decreasing: %d' % totalDecreases)


subranges(windowList)