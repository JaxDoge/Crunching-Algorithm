61. Rotate List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    	if not head or not head.next:
    		return head 

    	# get the length of linked nodes 

    	measure = head
    	list_size = 1
    	while measure.next:
    		measure = measure.next 
    		list_size += 1

    	real_k = k % list_size

    	p = q = head  
    	for _ in range(real_k):
    		q = q.next 

    	if p == q:  # Which means real k is zero
    	    return head 
    	else:
	    	while q.next:
	    		p = p.next 
	    		q = q.next 

	    	new_head = p.next 
	    	q.next = head 
	    	p.next = None 

	    	return new_head 
