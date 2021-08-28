141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 双倍速率快慢指针

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
    	if not head: return False 
    	if not head.next: return False 

    	p = head  
    	q = head.next  

    	while q.next and q.next.next:
    	    
    	    q = q.next 
    	    # Check the status at each q's step
    	    if q == p:
    	    	return True
    	    else:
    	    	q = q.next 
    	    if q == p:
    	        return True

    	    p = p.next 

        return False