199. Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 层序遍历最右边那个节点
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        from collections import deque
        projection_right_list = []
        node_queue = deque()
        node_queue.append(root)

        while node_queue:
        	sub_queue_size = len(node_queue)
        	for i in range(sub_queue_size):
        		pop_node = node_queue.popleft()
        		# 每层遍历到最后一个节点
        		if i == sub_queue_size -1:
        			projection_right_list.append(pop_node.val)
        		if pop_node.left:
        			node_queue.append(pop_node.left)
        		if pop_node.right:
        			node_queue.append(pop_node.right)
        return projection_right_list
