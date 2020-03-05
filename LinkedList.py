'''
Linked List : A linear data structure that holds data linked by pointers.

Pros over arrays
1) Dynamic size
2) Ease of insertion/deletion

Cons 
1) Access takes O(n) time since we have to start at the first node every time
2) Extra memory space is required for a pointer
3) No reference to each element

The linked list contains a sequence of nodes, which are instantiated with
data and a pointer to the next node.
'''


'''
We first define the node, with which each site can be instatiated.
'''

class Node:
	def __init__(self, data):
		self.val = data
		self.next = None
'''
With this, each node can contain data, and a pointer to next node (self.next)
can be used to link the nodes.
'''

'''
To define a linked list, we first define the head of the linked list, which
is the starting node of the list.
'''
class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.val)
			temp = temp.next
'''
This is a very simple implementation of a linked list, without any methods
'''

linked_list = LinkedList()
linked_list.head = Node(1)
first = linked_list.head
second = Node(2)
third = Node(3)

first.next = second
second.next = third

print(first.val) # == 1
print(first.next.val) # == (second.val)
print(first.next.next.val) # == (second.next.val) == (third.val)

print(linked_list.printList()) # 1 2 3 

'''
There are 3 types of linked list, 
1) Singly linked list
2) Doubly linked list
3) Circular linked list
'''

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.count = 0

	#Here the node is Node object
	def append(self, node):
		#if the list is empty 
		if self.head == None:
			#immediately assign node as head
			self.head = node
			
		else:
			curr = self.head

			#Loop until we see None pointer, which we can assign our node to
			while curr.next != None:
				curr = curr.next
			
			curr.next = node

	#Return the first index at which data is seen 
	def getdataIndex(self, data):
		curr = self.head
		index = 0

		#while the current node is not None (e.g. we reached the end of the list)
		while curr:
			if curr.val != data:
				curr = curr.next
				index += 1

			else:
				return index

		#no such data is found
		return -1

	#Insert a new node at the given index (<= length of the list)
	def insertNodeIndex(self, node, index):
		#previous and current Nodes at the beginning
		prev = None
		curr = self.head

		#index that works as counter of nodes
		curr_index = 0

		#Want to put new node to first index
		if index == 0:
			#If the head is not None
			if curr:
				#Temporary space for current head
				next_node = self.head
				#Assignment of new head as our new node
				self.head = node
				#Set a pointer to our temporary current head
				self.head.next = next_node
			else:
				self.head = node

		else:
			while curr_index < index:
				if curr:
					prev = curr
					curr = curr.next
				else:
					break

				curr_index += 1
			
			if curr_index == index:
				node.next = curr
				prev.next = node
			else:
				return -1

	#Add new node before the given data
	def insertNodedata(self, data, node):
		index = self.getdataIndex(data)
		if index >= 0:
			self.insertNodeIndex(node, index)

		else:
			return -1

	#Delete data at give index
	def deletedataIndex(self, index):
		current_index = 0
		curr = self.head
		prev = None
		next_node = self.head.next

		if index == 0:
			self.head = self.head.next

		else:
			while current_index < index:
				if curr.next:
					prev = curr
					curr = next_node
					next_node = curr.next

				else:
					break

				current_index += 1

			if current_index == index:
				prev.next = next_node

			else:
				return -1

	def print(self):
		curr = self.head
		linked_list = ""

		while curr:
			linked_list += str(curr.val)

			if curr.next:
				linked_list += "->"

			curr = curr.next
		print(linked_list)
  
	#Empty linked list
	def clear(self):
		self.head = None

