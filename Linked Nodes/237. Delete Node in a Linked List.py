237. Delete Node in a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# 只能像数组列表一样改node值了
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        while True:
        	if not cur.next.next:
        		cur.val = cur.next.val
        		cur.next = None
        		break
        	cur.val = cur.next.val
        	cur = cur.next

        return 


# 其实只要交换一次 node 值就可以了，不需要一直遍历
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return