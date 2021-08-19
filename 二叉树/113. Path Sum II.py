113. Path Sum II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    	paths_list = []
    	def preorderTraver(node, target, single_path = []):
    		nonlocal paths_list
    		if not node: return   # Do nothing
    		
    		# single_path.append(node.val)   #  这种写法不对，single_path 变量在递归过程中一直被修改，但理论上发现一个路径以后，该变量应该要置为空list
    		target -= node.val
            if target == 0 and not node.left and not node.right:
            	paths_list.append(single_path + [node.val])  # 这种写法生成了新变量，原有传入的 single_path 参数没有变化
            	return
            preorderTraver(node.left, target, single_path + [node.val])
            preorderTraver(node.right, target, single_path + [node.val])
            return

        preorderTraver(root, targetSum)
        return paths_list
