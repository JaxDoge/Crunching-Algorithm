147. Insertion Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def insertionSortList(self, head: ListNode | None) -> ListNode | None:
		if not head or not head.next:
			return head

		dummy_head = ListNode(-5001, next = head)
		last_sorted = head
		cur = head.next

		while cur:
			if cur.val >= last_sorted.val:
				last_sorted = cur
			else:
				navigator = dummy_head
				while navigator.next.val < cur.val:
					navigator = navigator.next
				
				last_sorted.next = cur.next
				cur.next = navigator.next
				navigator.next = cur
			
			cur = last_sorted.next
		
		return dummy_head.next





