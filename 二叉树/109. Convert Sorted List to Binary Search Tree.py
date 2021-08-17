109. Convert Sorted List to Binary Search Tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 快慢指针
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
    	# badcase
    	if not head: return None

    	def locateRoot(start: ListNode, end: ListNode):
    		p, q = head
    		while p != end and p.next != end:
    			if p.next.next:    # 如果p正好在倒数第一个节点，避免报错
    			    p = p.next.next 
    			else:
    				p = p.next
    			q = q.next
    		return q

    	def treeConstructor(head: ListNode, end: ListNode):
            if head == end:
            	return None

    		root_listnode = locateRoot(head,end)
    		root_val = root_listnode.val
    		root = TreeNode(val = root_val)
            root.left = treeConstructor(head,root_listnode)
            # 需要修改，搞简单了
            root.right = treeConstructor(root_listnode.next,end)
            return root
        res = treeConstructor(head, None)
        return res

