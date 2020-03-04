'''
Queue : Data structure for FIFO (First In, First Out)

'''

'''
Extremely simple version of queue. 
'''
class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, x):
		self.queue.append(x)

	def dequeue(self):

		if self.queue:
			return self.queue.pop(0)
		else:
			raise IndexError("The Queue is Empty")
			return None

	def max(self):
		return max(self.queue)

'''
Linked-List version of queue
'''