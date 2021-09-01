203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
    	if not head: return None

    	dummy_head = ListNode(val = 0, next = head)
        pre = dummy_head 
        cur = head 

        while True:
        	if not cur: break
        	if cur.val == val:
        		pre.next = cur.next
        		cur.next = None
        		cur = pre.next
        	else:
        		pre = cur
        		cur = cur.next
        return dummy_head.next
