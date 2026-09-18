86. Partition List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def partition(self, head: ListNode, x: int) -> ListNode:
		# x could larger than any of node value 

		# bad case 
		if not head or not head.next:
			return head 
		p = head 
		# we need a dummy head and a dummy median 

		dummy_head = q = ListNode(val = -300)
		dummy_median = r = ListNode(val = x)
		dummy_head.next = dummy_median

		while p:     # If the terminate condition is p.next, the last node would not be processed, even p is there
			p_next = p.next
			if p.val < x:
				q.next = p
				p.next = dummy_median
				p = p_next
				q = q.next

			else:
				r.next = p 
				p.next = None 
				p = p_next
				r = r.next 

		q.next = dummy_median.next 
		dummy_median.next = None 
		return dummy_head.next 



# p1 point to the last node the first part
# p2 point to the last node of the second part
# p3 point to the next node that need to be decided
class Solution:
	def partition(self, head: ListNode | None, x: int) -> ListNode | None:
		if not head or not head.next:
			return head

		dummy_head = ListNode()
		dummy_head.next = head
		p1 = dummy_head
		
		while p1.next and p1.next.val < x:
			p1 = p1.next

		p2 = p1.next

		# Corner case. already sorted
		if not p2:
			return head
			
		while p2 and p2.next and p2.next.val >= x:
			p2 = p2.next
		
		p3 = p2.next
		while p3:
			if p3.val < x:
				p2.next = p3.next
				p3.next = p1.next
				p1.next = p3

				p3 = p2.next
				p1 = p1.next
			else:
				p2 = p3
				p3 = p3.next
				
		return dummy_head.next     



