82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 双指针玩法
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    	if not head and not head.next:
    		return head 

    	p = q = head    
    	while q.next:
    		q = q.next 
    		if p.val != q.val:
    			p = q 

    		else:
    			p.next = q.next 
    			q.next = None 
    			q = p.next 

    	return head 