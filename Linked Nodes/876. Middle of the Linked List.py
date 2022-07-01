876. Middle of the Linked List


# Fast-slow pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head

        slow = head
        fast = head

        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                break

        return slow

