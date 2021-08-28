92. Reverse Linked List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代解法
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head: return head
        dummy_head = ListNode(val = -1)
        dummy_head.next  = head
        pre = dummy_head

        # Set pre as the node before left node
        for _ in range(left-1):
        	pre = pre.next  

        cur = pre.next # so cur start from left node

        for _ in range(right-left):
        	next_node = cur.next 
        	cur.next = next_node.next 
        	next_node.next = pre.next 
        	pre.next = next_node

        return dummy_head.next   # Never return dummy head itself




# 递归解法，空间复杂度高

class Solution:
    def __init__(self):
        self.successor = None   # The head.next may not be None at this scenario


    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1: # Special case, return last not head
            return self.reverseTopN(head, right)

        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head 



    def reverseTopN(self, node: ListNode, n: int):
        if n == 1:    # Only one node left
            self.successor = node.next
            return node 

        last_node = self.reverseTopN(node.next, n-1)
        node.next.next = node 
        node.next = self.successor
        return last_node

