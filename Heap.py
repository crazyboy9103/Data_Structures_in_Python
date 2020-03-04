'''
Heaps: This is an implementation of priority queue, which
can be visualized as a nearly complete binary tree. (Nearly with 
height lg(N)) Max heap property is that the key of a node is 
always greater than or equal to the keys of its children. 

We would like it to perform the followings: 
Insert(S, x) : Insert element x into the set S
Max(S) : Return element of S with the largest key
Extract_max(S) : Remove the Max(S) from S
Increase_key(S, x, k) : Increase the value of x's key to k

Root of tree :  first element in the array (i = 1)
parent(i) = i/2 : index of node's parent
left(i) = 2i :  index of node's left child
right(i) = 2i + 1 : index of node's right child

On such heap, we want to carry out these operations:
build_max_heap :  produce a max-heap from an unordered array
max_heapify : correct a single violation of max heap property 
			  in a subtree at its root
'''

class Heap:
	def __init__(self, array):
		self.array = array
		# Array of length N that we want to heap-ify

	def parent(self, i):
		return i/2

	def left(self, i):
		return 2*i

	def right(self, i):
		return 2*i+1

	def heap_size(self):
		return len(self.array)

	def max_heapify(self, i):
		#i is an index at which a single violation of max heap
		#property is seen
		# O(lg N) 
		l = self.left(i)
		r = self.right(i)

		index_largest = i
		if l <= self.heap_size() and self.array[l] > self.array[i]:
			index_largest = l
		

		if r <= self.heap_size() and self.array[r] > self.array[index_largest]:
			index_largest = r

		if index_largest != i:
			self.array[i], self.array[index_largest] = self.array[index_largest], self.array[i]

		self.max_heapify(index_largest)

	def build_max_heap(self):
		N = self.heap_size()
		
		for i in range(N/2, 1, -1):
			self.max_heapify(i)
		#The index starts from N/2 to 1 since those are the indices of all 
		#leaves of the tree (Draw a diagram to check this)
