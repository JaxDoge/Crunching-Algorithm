450. Delete Node in a BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
	def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
		node = root

	    def deleteIt(node, key):
	        if not node: return node 
	    	
	    	if key == node.val:
	    		#  Situation I: the node has no left or right node, or neither, replace the node with another child node, or just with None
	    		if not node.left:
	    			return node.right  # if node.right is None, it is still OK
	    		if not node.right:
	    			return node.left

	    		# Situation II: both left and right nodes are exisit, find the minium node in the right subtree or the maxium node in the right tree
                min_node_right = get_min(node.right)
                node.val = min_node_right.val
                # Delete the original node
                node.right = deleteIt(node.right, node.val)
            elif key > node.val:
            	node.right = deleteIt(node.right, key)
            elif key < node.val:
            	node.left = deleteIt(node.left, key)
            return node 

        def get_min(node):
        	while node.left:
        		node = node.left
        	return node 
        
        return deleteIt(node,key)