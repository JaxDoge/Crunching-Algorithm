83. Remove Duplicates from Sorted List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		if not head or not head.next:
			return head 

		p = q = head    
		while q.next:
			q = q.next 
			if p.val != q.val:
				p = q 

			else:
				p.next = q.next 
				q.next = None 
				q = p

		return head     	


class Solution:
	def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
		if not head or not head.next:
			return head

		p1 = p2 = head

		while p2:
			while p2.next and p2.val == p2.next.val:
				p2 = p2.next
			p2 = p2.next
			p1.next = p2
			p1 = p2

		return head