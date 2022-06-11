剑指 Offer 06. 从尾到头打印链表




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        helpStack = []
        while head:
            helpStack.append(head.val)
            head = head.next

        ans = []
        while helpStack:
            ans.append(helpStack.pop())

        return ans
