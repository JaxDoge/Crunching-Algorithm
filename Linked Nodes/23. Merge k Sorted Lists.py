23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# 分治方法

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    	# bad case
    	if not lists: return None 
    	if lists == [[]]: return None  

    	def mergeTwoLists(l1: ListNode, l2: ListNode):
	    	if not l1: return l2 
	    	if not l2: return l1 

	        # dummy_head 

	        dummy_head = ListNode(val = -1)
	        
	        # start point
	        frog = dummy_head

	        while l1 and l2:

		        if l1.val <= l2.val:
		        	# Remember, use a node firstly, change it secondly
		        	frog.next = l1
		        	l1 = l1.next
		        	frog = frog.next
		        else:
		        	frog.next = l2
		        	l2 = l2.next 
		        	frog = frog.next 

	        # add what left out to the end 
	        if l1:
	        	frog.next = l1
	        else:
	        	frog.next = l2

	        return dummy_head.next    		 

    	def mergeRecursion(lists, left: int, right: int):
    		# The bounce out condition
    		if left == right:
    			return lists[left]
    		if left > right: 
    			return None 

    		# middle point 
    		mid = (left+right) >> 1 
    		l1 = mergeRecursion(lists,left,mid)
    		l2 = mergeRecursion(lists,mid+1,right)

    		return mergeTwoLists(l1,l2)

    	merge_result = mergeRecursion(lists, 0, len(lists)-1)
    	return merge_result




