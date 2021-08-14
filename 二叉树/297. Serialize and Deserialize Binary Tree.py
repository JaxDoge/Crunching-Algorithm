297. Serialize and Deserialize Binary Tree


# Serialize and Deserialize come together, always

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



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

class Codec:
    import collections
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # badcase

        if not root: return '#'

        serialize_tree = []
        node = root
        helper = collections.deque()
        helper.append(node)
        while len(helper):
            ele = helper.popleft()
            if ele == '#':    # if ele is a Null TreeNode
                serialize_tree.append(ele)
                continue

            serialize_tree.append(ele.val)
            if ele.left:
                helper.append(ele.left)
            else:
                helper.append('#')
            if ele.right:
                helper.append(ele.right)
            else:
                helper.append('#')

        res = ','.join(map(str,serialize_tree))
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # badcases
        if not data or data == '#': return None

        deserialize_tree = list(data.split(','))
        res = TreeNode()
        
        helper = collections.deque()
        index = 0
        res.val = deserialize_tree[index]
        helper.append(res)

        while len(helper):
            node = helper.popleft()
  
            index += 1
            if index >= len(deserialize_tree):
                return res

            if deserialize_tree[index] != '#':    
                node.left = TreeNode(deserialize_tree[index])
                helper.append(node.left)

            index += 1
            if index >= len(deserialize_tree):
                return res

            if deserialize_tree[index] != '#':
                node.right = TreeNode(deserialize_tree[index])
                helper.append(node.right)   
        return res