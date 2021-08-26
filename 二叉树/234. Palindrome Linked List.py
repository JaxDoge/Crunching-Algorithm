234. Palindrome Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




# 快慢指针+二分
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
    	# bad case 1
        if not head: return False  
        # bad case 2
        if not head.next: return True
        dummy_head = ListNode(val = -1, next = head)
        p = q = dummy_head

        # 快慢指针一般写法
        while p and p.next:
            if p.next.next:
                p = p.next.next 
            else:
                p = p.next
            q = q.next 
        

        # 单数情况: q 是中间节点
        # 双数情况: p 是左半边最后节点

        q.next = self.subReverse(q.next) 


        # 双指针遍历
        left = dummy_head.next
        right = q.next 

        while right:
           
            if left.val != right.val:
                return False 
            left = left.next 
            right = right.next 
        return True

    def subReverse(self, start):
        pre = None 
        cur = node_next = start 
        while cur:
            node_next = cur.next 
            cur.next = pre 
            pre = cur  
            cur = node_next 
        return pre



