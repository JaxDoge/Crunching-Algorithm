103. Binary Tree Zigzag Level Order Traversal

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 层序遍历
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    	if not root: return None
    	
    	from collections import deque
    	res = []
    	helper = deque()
    	helper.append(root)
    	zigzag_flag = True

    	while helper:
    		sub_list = []
    		sub_queue_size = len(helper)  # 每层遍历节点数
    		for i in range(sub_queue_size):
    			if zigzag_flag:
    			    ele = helper.popleft()
				    sub_list.append(ele.val)
				    if ele.left:
				    	helper.append(ele.left)
				    if ele.right:
				    	helper.append(ele.right)
				else:
                	ele = helper.pop()
                    sub_list.append(ele.val)
                    # 入栈的顺序，左右也要反过来！！
                    if ele.right:
                    	helper.appendleft(ele.right)
                    if ele.left:
                    	helper.appendleft(ele.left)


    	        i += 1
            res.append(sub_list)
    	    # 改变标识符方向
            zigzag_flag = not zigzag_flag
        return res
