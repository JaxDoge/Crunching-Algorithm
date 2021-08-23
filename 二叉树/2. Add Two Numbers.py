2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    	
    	head = res = ListNode(val = 0)
    	carry = 0    # Record carry value
    	while l1 and l2:

    		sumup = l1.val + l2.val + carry
    		carry = 0
    		l1 = l1.next 
    		l2 = l2.next 
    		if sumup > 9:
    			res.next = ListNode(val = int(sumup % 10))
    			carry = 1

    		else:
    			res.next = ListNode(val = sumup)
    		res = res.next


    	if not l1:
    		while l2:
    			sumup = l2.val + carry
    			carry = 0
    			l2 = l2.next
	    		if sumup > 9:
	    			res.next = ListNode(val = int(sumup % 10))
	    			carry = 1
	    		else:
	    			res.next = ListNode(val = sumup)
	    		res = res.next

    	if not l2:
    		while l1:
    			sumup = l1.val + carry
    			carry = 0
    			l1 = l1.next
	    		if sumup > 9:
	    			res.next = ListNode(val = int(sumup % 10))
	    			carry = 1
	    		else:
	    			res.next = ListNode(val = sumup)
	    		res = res.next
             
        if carry != 0:
        	res.next = ListNode(val = carry)
        	carry = 0
    	return head.next
