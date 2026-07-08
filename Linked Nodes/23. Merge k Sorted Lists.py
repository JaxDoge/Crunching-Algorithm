23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# 分治方法

class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		n = len(lists)
		if not n:
			return None

		def mergeTwoLists(l1, l2):
			if not l1: return l2
			if not l2: return l1

			head = curr = ListNode()

			while l1 and l2:
				if l1.val <= l2.val:
					curr.next = l1
					l1 = l1.next
				else:
					curr.next = l2
					l2 = l2.next
				curr = curr.next

			if l1:
				curr.next = l1
			else:
				curr.next = l2
			return head.next

		def mergeRecursion(lists, left, right):
			if left == right:
				return lists[left]

			mid = (left + right) >> 1
			l1 = mergeRecursion(lists, left, mid)
			l2 = mergeRecursion(lists, mid + 1, right)

			return mergeTwoLists(l1, l2)
		
		return mergeRecursion(lists, 0, n - 1)
		




