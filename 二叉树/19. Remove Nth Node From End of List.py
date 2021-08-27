19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# 双指针法，空间复杂度 O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next: return None 
        dummy_head = ListNode(val = -1, next = head)
        first = second = dummy_head 

        # move second pointer n-1 step ahead
        for _ in range(n):
        	second = second.next 

        while second.next:
        	first = first.next 
        	second = second.next

        # first point to he predecessor of target node 

        delete_node = first.next 
        first.next = delete_node.next 
        delete_node.next = None 

        del delete_node
        return dummy_head.next 




 	







