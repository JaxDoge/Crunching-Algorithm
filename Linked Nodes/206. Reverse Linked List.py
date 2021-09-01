206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    	cur = head
    	# define a pre pointer
    	pre = None
    	while cur:
    	    next_node = cur.next
    	    cur.next = pre
    	    pre = cur 
    	    cur = next_node
    	return pre
