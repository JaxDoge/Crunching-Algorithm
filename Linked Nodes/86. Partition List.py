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






