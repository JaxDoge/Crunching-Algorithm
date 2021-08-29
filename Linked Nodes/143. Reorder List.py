143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 快慢指针
# 反转后半段链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return

        def reverseSublist(start):  # Classical approach for reversing a linked node list
        	pre = None 
        	while start:
        		next_node = start.next 
        		start.next = pre 
        		pre = start 
        		start = next_node
        	return pre

        fast, slow = head, head 

        # 这种方法 slow 会指向中间节点（奇数），或者后半部分的开始节点（偶数）
        while True:
        	if not fast.next: break  
        	if fast.next.next:
        		fast = fast.next.next 
        	else:
        		fast = fast.next  
        	slow = slow.next 

        cur = head  
        
        # reorder 以后 slow.next 必然处于最后一个节点，也就是翻转的起始位置
        # fast 已经指向最后的节点，所以直接成为了翻转后的头节点
        reverseSublist(slow.next)
        slow.next = None 

        slow = head 
        while True:
        	if not fast: break
        	next_node = slow.next 
        	slow.next = fast
        	fast = fast.next 
        	slow.next.next = next_node
        	slow = next_node

        return 




