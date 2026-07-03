716. Max Stack

# Heapq + Double linked node

class HeapItem:
	def __init__(self, value = 0, index = 0, linkedNode = None):
		self.value = value
		self.index = index
		self.linkedNode = linkedNode

class LinkedNode:
	def __init__(self, value = 0, heapItem: HeapItem = None):
		self.value = value
		self.heapItem = heapItem
		self.order = -1
		self.prev = None
		self.next = None

class MaxStack:

	def __init__(self):
		self.heap = []
		self.head = LinkedNode()
		self.tail = LinkedNode()
		self.head.next = self.tail
		self.tail.prev = self.head
		
	def _add_node(self, node: LinkedNode):
		old_last = self.tail.prev
		node.order = old_last.order + 1

		old_last.next = node
		node.next = self.tail

		self.tail.prev = node
		node.prev = old_last

	def _remove_node(self, node: LinkedNode):
		prev = node.prev
		nxt = node.next

		prev.next = nxt
		nxt.prev = prev

	def _parent(self, i):
		return (i - 1) // 2

	def _left_child(self, i):
		return i * 2 + 1

	def _right_child(self, i):
		return i * 2 + 2

	def _has_higher_priority(self, item_a: HeapItem, item_b: HeapItem):
		if item_a.value != item_b.value:
			return item_a.value > item_b.value
		# Tie breaker
		return item_a.linkedNode.order > item_b.linkedNode.order

	def _down_heap_item(self, heap_item: HeapItem):

		n = len(self.heap)
		left_index = self._left_child(heap_item.index)
		right_index = self._right_child(heap_item.index)
		largest_index = heap_item.index

		if left_index < n and self._has_higher_priority(self.heap[left_index], self.heap[largest_index]):
			largest_index = left_index

		if right_index < n and self._has_higher_priority(self.heap[right_index], self.heap[largest_index]):
			largest_index = right_index

		if largest_index != heap_item.index:
			self.heap[heap_item.index], self.heap[largest_index] = self.heap[largest_index], self.heap[heap_item.index]
			# Update item object index
			self.heap[heap_item.index].index, heap_item.index = heap_item.index, self.heap[heap_item.index].index

			self._down_heap_item(heap_item)


	def _up_heap_item(self, heap_item: HeapItem):
		if heap_item.index == 0:
			return

		parent_item_index = self._parent(heap_item.index)
		parent_item = self.heap[parent_item_index]

		if self._has_higher_priority(parent_item, heap_item):
			return

		self.heap[heap_item.index], self.heap[parent_item_index] = self.heap[parent_item_index], self.heap[heap_item.index]
		# Update item object index
		self.heap[heap_item.index].index, heap_item.index = heap_item.index, self.heap[heap_item.index].index
		self._up_heap_item(heap_item)

	def _remove_heap_item(self, heap_item: HeapItem):
		n = len(self.heap)

		if heap_item.index != n - 1:
			original_index = heap_item.index
			self.heap[original_index], self.heap[n - 1] = self.heap[n - 1], self.heap[original_index]
			# Exchange object index as well
			self.heap[original_index].index, heap_item.index = heap_item.index, self.heap[original_index].index
			self.heap.pop()

			# The uprised heap item may need to be push up or push down.
			# Comparing with its parent
			if original_index > 0 and self._has_higher_priority(self.heap[original_index], self.heap[self._parent(original_index)]):
				self._up_heap_item(self.heap[original_index])
			else:
				self._down_heap_item(self.heap[original_index])
		else:
			self.heap.pop()

	def push(self, x: int) -> None:
		new_linked_node = LinkedNode(x)
		new_heap_item = HeapItem(x, index = len(self.heap))

		new_linked_node.heapItem = new_heap_item
		new_heap_item.linkedNode = new_linked_node

		self._add_node(new_linked_node)

		self.heap.append(new_heap_item)
		self._up_heap_item(new_heap_item)


	def pop(self) -> int:
		if self.head.next == self.tail:
			return None

		node = self.tail.prev

		# Remove from linked list
		self._remove_node(node)

		# Remove from heap
		heap_item = node.heapItem
		self._remove_heap_item(heap_item)

		return node.value
		

	def top(self) -> int:
		if self.head.next == self.tail:
			return None

		node = self.tail.prev
		return node.value
		

	def peekMax(self) -> int:
		if not self.heap:
			return None

		heap_item = self.heap[0]
		return heap_item.value
		

	def popMax(self) -> int:
		if not self.heap:
			return None

		heap_item = self.heap[0]
		node = heap_item.linkedNode

		# Remove from linked list
		self._remove_node(node)
		# Remove from heap
		self._remove_heap_item(heap_item)

		return heap_item.value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()