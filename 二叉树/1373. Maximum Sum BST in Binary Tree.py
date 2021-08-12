1373. Maximum Sum BST in Binary Tree

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left 
		self.right = right 

# 这里有个重要的新知识点，空树 TreeNode root = None 也是有 val，而且 val = 0

class Solution:
	def maxSumBST(self, root: TreeNode) -> int:
        result = 0  # 不会出现负数，直接从 0 开始计数
		# 该函数返回以 node 为根节点的树：
		# 是否是 bst，空树是 bst
		# 最小 val 值，空树该值为 Integer.Max_value
		# 最大 val 值，空树该值为 Integer.Min_value
		# 这样真实的叶子节点才是合法 BST
		# 该树所有节点值之和，空树该值为 0，superise MZFC!
		def traversal(node) -> List:
			nonlocal result
			# boundary conditions
			if not node:
				return [1, float('inf'), float('-inf'), 0]
            
            # 递归调用，得到左右子树的 res
			left_res = traversal(node.left)
			right_res = traversal(node.right)
            # 开始后序遍历
            res = [0] * 4
            # 这就是几个合法 BST 基本条件了，
            if left_res[0] and right_res[0] and left_res[2] < node.val and right_res[1] > node.val:
            	res[0] = 1 
            	res[1] = min(left_res[1],node.val)  # 兼容 left node 是空树的情况
            	res[2] = max(right_res[2],node.val)  # 兼容 right node 是空树的情况
            	res[3] = node.val + left_res[3] + right_res[3]
                result = max(result, res[3])
            return res 
        traversal(root)
        return result


