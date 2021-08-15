222. Count Complete Tree Nodes
#According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.left = None
#         self.right = None

# Design an algorithm that runs in less than O(n) time complexity.

# 2<<1 == 4 位运算

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        node = root
        left_node = node.left
        right_node = node.right
        
        # Calculate the height of left subtree 	
        left_height = 0
        while left_node:
        	left_node = left_node.left 
        	left_height += 1

        # Calculate the height of right subtree
        right_height = 0
        while right_node:
        	right_node = right_node.right 
        	right_height += 1

        # Based on the definition of complete binary tree, one of it's subtrees is a perfect binary tree
        if left_height == right_height: # if node is the root of a perfect tree
            return (2<<left_height)-1
        return 1+self.countNodes(node.left)+self.countNodes(node.right)