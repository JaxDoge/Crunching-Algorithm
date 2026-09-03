19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		dummy_head = ListNode()
		dummy_head.next = head
		p1 = dummy_head
		p2 = head

		for _ in range(n - 1):
			p2 = p2.next

		while p2.next:
			p1 = p1.next
			p2 = p2.next

		target = p1.next
		p1.next = target.next

		return dummy_head.next




	







