arr = [1,6,103,91,4,21,13,21,2,3]

def binarySearch(arr, left, right):

	if left == right:
		return arr[left]
	if left == right - 1:
		if arr[left] > arr[right]:
			return arr[left]
		else:
			return arr[right]

	mid = int((left+right)/2)
	
	leftMax = binarySearch(arr, left, mid)
	rightMax = binarySearch(arr, mid+1, right)

	if leftMax > rightMax:
		return leftMax
	else:
		return rightMax

print(binarySearch(arr, 0, len(arr)-1))