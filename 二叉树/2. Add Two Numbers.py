# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        carry = 0

        while l1 and l2:
            sum_up = l1.val + l2.val + carry

            l1 = l1.next
            l2 = l2.next
            carry = 0

            if sum_up > 9:
                carry = 1
                curr.next = ListNode(val = sum_up % 10)
            else:
                curr.next = ListNode(val = sum_up)

            curr = curr.next

        def one_list(l):
            nonlocal carry, curr
            sum_up = l.val + carry
            l = l.next
            carry = 0

            if sum_up > 9:
                carry = 1
                curr.next = ListNode(val = sum_up % 10)
            else:
                curr.next = ListNode(val = sum_up)

            curr = curr.next     
            return l 


        while l2:
            l2 = one_list(l2)

        while l1:
            l1 = one_list(l1)

        if carry:
            curr.next = ListNode(val = carry)
        
        return head.next