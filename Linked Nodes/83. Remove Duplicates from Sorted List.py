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