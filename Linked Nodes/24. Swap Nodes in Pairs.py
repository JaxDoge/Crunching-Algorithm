24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# 递归解法
class Solution:
	# def __init__(self, head: ListNode):
	# 	self.dummy_head = ListNode(val = -1, next = head)

	def swapPairs(self, head: ListNode) -> ListNode:
		if not head or not head.next:
			return head
		successor = head.next.next 
		new_head = head.next
		new_head.next = head
		head.next = self.swapPairs(successor)
		return new_head


# 迭代解法

class Solution:
	def swapPairs(self, head: ListNode) -> ListNode:
		if not head or not head.next:
			return head 

		dummy_head = ListNode(val = -1, next = head)

		pre = dummy_head
		 

		while head and head.next:
			next_node = head.next
			pre.next = next_node
			head.next = next_node.next 
			next_node.next = head 

			pre = head
			head = head.next

		
		return dummy_head.next 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		dummy_head = ListNode()
		dummy_head.next = head

		p1 = dummy_head
		p2 = p1.next
		if not p2:
			return None
		p3 = p2.next
		if not p3:
			return head
		
		while p3 and p2:
			p2.next = p3.next
			p3.next = p2
			p1.next = p3

			p2 = p1.next
			p3 = p2.next

			if not p3.next or not p3.next.next:
				break

			p3 = p3.next.next
			p2 = p2.next.next
			p1 = p1.next.next

		return dummy_head.next