95. Unique Binary Search Trees II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 递归解法
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
    	# Handle badcase
    	if not n: return []  # if n is zero, return empty list

    	def builder(low: int, high: int) -> List[TreeNode]:
    		res = []    # all the possible trees (root nodes)
    		# Handle boundary conditions, the last node has two None subtrees
    		if low > high:
    			res.append(None)
    			return res

    		for root in range(low, high+1):
    			# 递归计算左右子树的所有合法bst构型, 返回对应的根节点list
    			left_trees_list = builder(low, root-1)
    			right_trees_list = builder(root+1, high)
                
                #有了递归结果以后，直接构造树就完事了
                # 这就是笛卡尔积
    			for left_tree in left_trees_list:
    				for right_tree in right_trees_list:
    					root_node = TreeNode(val = root)
    					root_node.left = left_tree
    					root_node.right = right_tree 
                        
                        # record result
                        res.append(root_node)
            return res 
        return builder(1,n)

