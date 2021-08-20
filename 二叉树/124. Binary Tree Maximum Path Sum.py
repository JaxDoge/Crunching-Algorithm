124. Binary Tree Maximum Path Sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归解法
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
    	res = float('-inf')
    	# 从底向上的逻辑，后序遍历
    	def backorder(node):
    		nonlocal res
    		if not node: return 0
            
            # 一旦一边子树返回的最大路径和是个负数，直接抛弃这边的子树即可，因为任何情况下都不会大于当前节点本身的值
            left_path_sum = max(backorder(node.left),0)
            right_path_sum = max(backorder(node.right),0)

    		sub_sum = max(node.val+left_path_sum, node.val+right_path_sum)
    		# 最大值有可能出现在通过当前节点链接左右子树路径的情况下
    		res = max(res, node.val+left_path_sum+right_path_sum)
    		return sub_sum
    	backorder(root)
    	return res