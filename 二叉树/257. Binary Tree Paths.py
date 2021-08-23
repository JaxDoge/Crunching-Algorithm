257. Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
    	res = []
        
        def preorder(node, sub_list = []):
        	if not node: return
        	sub_list.append(str(node.val))
        	if not node.left and not node.right:
        		res.append('->'.join(sub_list))
        		sub_list.pop()
        		return
        	preorder(node.left, sub_list)
        	preorder(node.right, sub_list)
            sub_list.pop()
        	return

        preorder(root)
        return res






