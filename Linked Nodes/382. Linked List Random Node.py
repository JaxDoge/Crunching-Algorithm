382. Linked List Random Node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import randrange
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        p = self.head
        res = 0
        i = 1
        while p:
            r = randrange(i)
            if r == 0:
                res = p.val 
            p = p.next
            i += 1
        
        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()