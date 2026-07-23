428. Serialize and Deserialize N-ary Tree


"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
		if children is None:
			children = []
		self.val = val
		self.children = children
"""

class Codec:
	def serialize(self, root: 'Node') -> str:
		"""Encodes a tree to a single string.
		
		:type root: Node
		:rtype: str
		"""
		serialize_list = []
		def helper(node, serialize_list):
			if not node:
				return

			# serialize val
			serialize_list.append(chr(node.val))
			# serialize number of children
			serialize_list.append(chr(len(node.children)))

			for ch in node.children:
				 helper(ch, serialize_list)

		helper(root, serialize_list)
		return "".join(serialize_list)
		
	
	def deserialize(self, data: str) -> 'Node':
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: Node
		"""
		if not data:
			return None

		idx = 0

		def helper():
			nonlocal idx

			if idx == len(data):
				return None

			val = ord(data[idx])
			idx += 1
			number_of_ch = ord(data[idx])
			idx += 1

			new_node = Node(val = val)

			for _ in range(number_of_ch):
				child_node = helper()
				if child_node:
					new_node.children.append(child_node)

			return new_node

		return helper()

		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))