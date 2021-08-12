297. Serialize and Deserialize Binary Tree


# Serialize and Deserialize come together, always

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# Preorder method
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        serial_tree = []  # List[String]
        def helper(node):
        	nonlocal serial_tree
        	if not node:
        	    serial_tree.append('#')
                return
            serial_tree.append(str(node.val))
            helper(node.left)
            helper(node.right)
        return ','.join(serial_tree)



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        deserialize_tree = list(data.split(','))
        deserialize_tree.reverse()
        def helper(tree_list):
        	if tree_list == ['#'] or not tree_list:
        		return None 
            # Convert string to list
            if tree_list[-1] == '#':
            	tree_list.pop()
                return None
            

        	node = TreeNode(int(tree_list.pop()))
        	
        	node.left = helper(tree_list)
        	node.right = helper(tree_list)
            return node 
        return helper(deserialize)




# 层序遍历