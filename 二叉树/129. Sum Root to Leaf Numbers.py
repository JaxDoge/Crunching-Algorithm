129. Sum Root to Leaf Numbers


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 后序遍历解法，考虑首数位是 0 的特殊情况，利用前序遍历找到所有首个根节点不为0的子树
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
    	nonzero_subtree_list = []
    	digital_list = []
    	def backorder(node):
    		if not node: return []
    		if not node.left and not node.right: return [str(node.val)]
    		left_num_list = backorder(node.left)
    		right_num_list = backorder(node.right)
            sub_digital_list = left_num_list + right_num_list
            for i in range(len(sub_digital_list)):
            	sub_digital_list[i] = str(node.val) + sub_digital_list[i]
    		return sub_digital_list

        def preorder(node):  # 寻找root节点不为 0 的最大子树
            nonlocal nonzero_subtree_list
            if not node: return 
            if node.val != 0:
            	nonzero_subtree_list.append(node)
            	return
            else:
            	preorder(node.left)
            	preorder(node.right)
                return
        
        preorder(root)
        for node in nonzero_subtree_list:
            digital_list.extend(backorder(node))

		res = sum([int(ele) for ele in digital_list])
		return res 


# 前序遍历，教科书解法

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
    	def preorder(node, cur_sum):
    		if not node: return 0    # no new digit
    		total_sum = cur_sum * 10 + node.val
    		if not node.left and not node.right:
    			return total_sum
    		
    		return preorder(node.left, total_sum) + preorder(node.right, total_sum)
    	return preorder(root,0)

