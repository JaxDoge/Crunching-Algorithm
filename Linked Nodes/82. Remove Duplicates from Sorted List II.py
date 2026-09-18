82. Remove Duplicates from Sorted List II





# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
		if not head or not head.next:
			return head

		dummy_head = ListNode()
		dummy_head.next = head
		p1 = dummy_head
		p2 = head
		p3 = head.next

		while p3:
			if p3.val == p2.val:
				p3 = p3.next
				continue
			
			if p2.next == p3:
				p1 = p2
				p2 = p2.next
				p3 = p3.next
			else:
				p1.next = p3
				p2 = p3
				p3 = p3.next
			
		if p2.next:
			p1.next = None
		else:
			p1.next = p2
		 
		return dummy_head.next