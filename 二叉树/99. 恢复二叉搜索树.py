99. 恢复二叉搜索树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # badcase

        if not root or (not root.left and not root.right): return
        
        node_list = []
        def inorderTraverser(node):
        	nonlocal node_list
        	if not node: return
        	inorderTraverser(node.left)

            node_list.append(node)
            inorderTraverser(node.right)
        
        def detector(node_list: [TreeNode]):
        	if not node_list: return
            p = 0
            q = len(node_list)-1
            stop_sign = 0

            while p < q and stop_sign < 2:
            	if node_list[p].val < node_list[p+1].val:
            		p += 1
            	else:
            		stop_sign += 1
            	if node_list[q].val > node_list[q-1].val:
            		q -= 1
            	else stop_sign += 1
            return p, q

        inorderTraverser(root)
        p, q = detector(node_list)
        if p >= q: return # 不需要修改bst 的情况
        node_list[p].val, node_list[q].val = node_list[q].val, node_list[p].val
        return

# Morris 解法, inorder traversal

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
		# badcase
		if not root: return

		node = root
        swap_list = []
        p = None
		while node:   # Before node traver to the ultra right
	        if not node.left:
	        	if p:
		        	if node.val < p.val and not swap_list:
	                    swap_list.extend([p, node])
	                elif node.val < p.val and len(swap_list) == 2:
	                	swap_list.pop()
	                	swap_list.append(node)
	        	p = node
	            node = node.right
	        else:
		        pred = node.left      # One step left
		        while pred.right and pred.right != node:
		        	pred = pred.right

		        if not pred.right:
		        	pred.right = node
		        	pred = None
		        	node = node.left 
		        else:    # left subtree has travered, go right
		        	if p:
			        	if node.val < p.val and not swap_list:
		                    swap_list.extend([p, node])
		                elif node.val < p.val and len(swap_list) == 2:
		                	swap_list.pop()
		                	swap_list.append(node)
	                p = node
		        	node = node.right
		        	pred.right = None   # break dummy link
        if len(swap_list) == 2:
        	swap_list[0].val, swap_list[1].val = swap_list[1].val, swap_list[0].val
	    return