617. Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# 官方的dfs可能存在问题，直接return t1，导致的是有一部分内存会和Tree1共享，修改官方代码后的结果
class Solution:
	def copyTree(self, node):
		if not node: return None
		new_node = TreeNode(node.val)
		new_node.left = self.copyTree(node.left)
		new_node.right = self.copyTree(node.right)
		return new_node

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
    	if not root1: return self.copyTree(root2)
    	if not root2: return self.copyTree(root1)

    	merge_tree = TreeNode(root1.val + root2.val)
    	merge_tree.left = self.mergeTrees(root1.left, root2.left)
    	merge_tree.right = self.mergeTrees(root1.right, root2.right)
    	return merge_tree
