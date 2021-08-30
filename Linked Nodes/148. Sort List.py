148. Sort List

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 归并排序 - 递归
class Solution:
    def sortList(self, head: ListNode) -> ListNode:





# 归并排序 - 迭代
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
    	def mergeTwoSortedLN(l1: ListNode, l2: ListNode):
	    	if not l1: return l2 
	    	if not l2: return l1 
	        dummy_head = ListNode(val = 0)
	        frog = dummy_head
	        while l1 and l2:
		        # frog's next point to the smaller node and then frog jump to it 
		        if l1.val <= l2.val:
		        	frog.next = l1
		        	l1 = l1.next
		        	frog = frog.next
		        else:
		        	frog.next = l2
		        	l2 = l2.next 
		        	frog = frog.next 

	        if l1:
	        	frog.next = l1
	        else:
	        	frog.next = l2
	        return dummy_head.next    	

	    if not head or not head.next: return head

	    hair_node = ListNode(val = 0, next = head)
	    list_size = 0
	    sublist_size = 1
	    cur = head

	    # Count the list length
	    while cur:
	        list_size += 1
	        cur = cur.next

        # End loop if the sublist size is equal or larger than the list size, because the final merge is finished 
	    while sublist_size < list_size:
	    	pre_node = hair_node
	    	cur = pre_node.next
	    	# Scan the whole linked nodes with auxiliary pointer cur during each sublist size level
	    	while cur:
		    	# find the h1 position, which is the cur obviously
		    	h1 = cur
		    	h2 = None
		    	# find the end of h1 list

		    	# Don't change the value of sublist_size !! Use while carefully!!
		    	step = sublist-1
		    	while step and cur:  # cur is not point out
		    		cur = cur.next
		    	    step -= 1
		    	# got the h2 position, if cur does not point to None
		    	# break the link between cur and h2
		    	if cur:
			    	h2 = cur.next
			    	cur.next = None
			    	cur = h2
		    	# find the end node of h2, if h2 does not point to None
		    	step = sublist-1
		        while h2 and cur and step:
		        	cur = cur.next
		        	step -= 1

		        # get the start node of the rest nodes, if they exist
		        # break the link between cur and succ_node, if succ_node exist
		        succ_node = None
		        if cur:
		        	succ_node = cur.next
		        	cur.next = None
		        	cur = succ_node


	            # merge h1 and h2, pre node point to the result
		        pre_node.next = mergeTwoSortedLN(h1,h2)
		        # move pre to the end of sub list, ready for next turn 
		        while pre_node.next:
		        	pre_node = pre_node.next

		        # double the sublist size
	        sublist_size <<= 1
	    return hair_node.next













