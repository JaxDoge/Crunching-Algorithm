111. Minimum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归解法
class Solution:
    def minDepth(self, root: TreeNode) -> int:
    	def lowestSubtree(node):
    		if not node: return 0
    		left_height = lowestSubtree(node.left)
    		right_height = lowestSubtree(node.right)
            # 需要考虑特殊情况，某个子树为空树，必然高度最小，但却不能返回这个子树的高度
    		if not left_height: return right_height + 1
    		if not right_height: return left_height +1
    		return min(left_height,right_height)+1

    	return lowestSubtree(root)

# 层序遍历解法
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        import collections
        node_queue = collections.deque()
        # traver_list = []                 # Maybe we don't need it
        height = 1             # Record current travesal height, start from one
        node_queue.append(root)

        while node_queue:
            sub_loop_num = len(node_queue)    # Record the number of nodes in this layer

            for i in range(sub_loop_num):
                pop_node = node_queue.popleft()
                if pop_node.left:
                    node_queue.append(pop_node.left)
                if pop_node.right:
                    node_queue.append(pop_node.right)
                if not pop_node.left and not pop_node.right:  # Found a leaf, it's the first leaf from left
                    return height

            height += 1
        return height







