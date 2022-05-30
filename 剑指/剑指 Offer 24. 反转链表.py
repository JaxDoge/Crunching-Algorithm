剑指 Offer 24. 反转链表



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next == None:
            return head

        resHead = head
        while resHead.next is not None:
            resHead = resHead.next

        def rev(node):
            if not node.next:
                return node

            nxt = rev(node.next)
            nxt.next = node
            node.next = None
            return node
        rev(head)
        return resHead
