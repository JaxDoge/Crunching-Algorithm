147. Insertion Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
    	if not head or not head.next: return head 

    	dummy_head = pre = ListNode(val = 0, next = head)
    	p = head 

    	while True:
    		if not p.next: break 
    		q = p
    		while q.next:
    			if p.val > q.next.val:
    				# change the position of p and q.next
    				q_next = q.next
    				p_next = p.next
    				pre.next = q_next
    				q.next = p
    				p.next = q_next.next
    				q_next.next = p_next    				





