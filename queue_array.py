class Queue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return str(self.queue)

	def enqueue(self, item):
		self.queue.append(item)
	
	def dequeue(self):
		item = self.queue[0]
		for i in range(len(self.queue)-1):
			self.queue[i] = self.queue[i+1]
		self.queue.pop()
		return item

	def isEmpty(self):
		if self.queue:
			return False
		return True

	def size(self):
		return len(self.queue)

def hotPotato(namelist, num):
	simqueue = Queue()
	for i in namelist:
		simqueue.enqueue(i)
	print(simqueue)
	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())
		simqueue.dequeue()
	return simqueue.dequeue()

n = 14.5
print(int(round(n)))

