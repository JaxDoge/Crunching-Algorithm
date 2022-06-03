剑指 Offer 22. 链表中倒数第k个节点




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Fast ans slow pointer

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head
        if not head:
            return None

        for _ in range(k - 1):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        return slow