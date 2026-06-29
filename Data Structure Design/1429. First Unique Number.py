1429. First Unique Number


class LinkNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.in_list = True

class FirstUnique:
	def __init__(self, nums: List[int]):
		self.appear_map = defaultdict(int)
		self.head = LinkNode()
		self.tail = LinkNode()
		self.head.next = self.tail
		self.tail.prev = self.head

		n = len(nums)

		for i in range(n):
			self.add(nums[i])

	def _add_node(self, node: LinkNode):
		# add a new node to the tail
		old_last = self.tail.prev
		
		old_last.next = node
		node.next = self.tail

		node.prev = old_last
		self.tail.prev = node
		
	def _remove_node(self, node: LinkNode):
		prev_node = node.prev
		next_node = node.next

		prev_node.next = next_node
		next_node.prev = prev_node

		node.in_list = False

	def showFirstUnique(self) -> int:
		if self.head.next == self.tail:
			return -1
		return self.head.next.key
		

	def add(self, value: int) -> None:
		if value in self.appear_map:
			cur_node = self.appear_map[value]
			cur_node.value += 1
			# remove the node if it is in the linked list
			if cur_node.in_list:
				self._remove_node(cur_node)

		else:
			new_node = LinkNode(value, 1)
			self.appear_map[value] = new_node
			self._add_node(new_node)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)