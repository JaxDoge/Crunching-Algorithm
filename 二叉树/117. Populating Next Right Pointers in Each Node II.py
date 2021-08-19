117. Populating Next Right Pointers in Each Node II


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 层序遍历解法，不能搞 O(1) 空间复杂度解法了
class Solution:
    def connect(self, root: 'Node') -> 'Node':
    	if not root: return

        from collections import deque
        node_queue = deque()
        node_queue.append(root)

    	while node_queue:
    		level_size = len(node_queue)
    		for i in range(level_size):
    			pop_node = node_queue.popleft()
    			if i < level_size-1:         # Otherwise we traver at the right most node of a level
    				pop_node.next = node_queue[0]
    			if pop_node.left:
    				node_queue.append(pop_node.left)
    			if pop_node.right:
    				node_queue.append(pop_node.right)
    			i += 1
        return



