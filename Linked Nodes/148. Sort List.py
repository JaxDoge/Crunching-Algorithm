148. Sort List

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next





class Solution:
	def sortList(self, head: ListNode | None) -> ListNode | None:
		def merge_two_sorted_ln(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
			if not l1: return l2
			if not l2: return l1
			dummy_head = ListNode(-1)
			needle = dummy_head
			while l1 and l2:
				if l1.val <= l2.val:
					needle.next = l1
					l1 = l1.next
					needle = needle.next
				else:
					needle.next = l2
					l2 = l2.next
					needle = needle.next
			
			if l1:
				needle.next = l1
			if l2:
				needle.next = l2
			
			return dummy_head.next

		if not head or not head.next:
			return head
		
		dummy_head = ListNode(-1, next = head)
		list_size = 0
		sub_size = 1
		cur = head

		while cur:
			list_size += 1
			cur = cur.next
		
		while sub_size < list_size:
			# pre_node point to the last sorted node in this round
			pre_node = dummy_head
			cur = pre_node.next

			while cur:
				# We need to isolate two sorted linked list
				h1 = cur
				h2 = None

				# find the end of h1
				for _ in range(sub_size - 1):
					if not cur: break
					cur = cur.next
				
				if cur:
					h2 = cur.next
					# disconnect to the rest node
					cur.next = None
					cur = h2
				
				# find the end of h2
				if h2:
					for _ in range(sub_size - 1):
						if not cur: break
						cur = cur.next
				
				# The start node of next iteration
				succ_node = None
				if cur:
					succ_node = cur.next
					cur.next = None
					cur = succ_node

				# Merge two sorted list
				pre_node.next = merge_two_sorted_ln(h1, h2)

				# pre_node always point to the last sorted node in this round
				while pre_node.next:
					pre_node = pre_node.next

			sub_size *= 2
		
		return dummy_head.next













