990. Satisfiability of Equality Equations

class UF:
	def __init__(self, count):
		self.count = count
		self.parent = [i for i in range(self.count)]
		self.size = [1] * count

	def find(self, node):
		while node != self.parent[node]:
			self.parent[node] = self.parent[self.parent[node]]
			node = self.parent[node]
		return node

	def union(self, p, q):
		rootP = self.find(p)
		rootQ = self.find(q)
		if rootP == rootQ:
			return

		if self.size[rootP] >= self.size[rootQ]:
			self.parent[rootQ] = rootP
			self.size[rootP] += self.size[rootQ]
		else:
			self.parent[rootP] = rootQ
			self.size[rootQ] += self.size[rootP]

		self.count -= 1

	def connected(self, p, q):
		rootP = self.find(p)
		rootQ = self.find(q)
		return rootP == rootQ


# ["a==b","b!=a"]
# 需要把字符映射成数字，最好的办法是寻找字符对应的 unicode, ord() 函数, 将 a~z 映射到 0~25
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
    	if not list: return False
        
        # There are 26 lowercase letters
        helper_uf = UF(26)
        # 联通所有相等的子树
        for ele in equations:
        	if ele[1] == '=':
        		node_1 = ord(ele[0]) - ord('a')
        		node_2 = ord(ele[3]) - ord('a')
        		helper_uf.union(node_1,node_2)

        # 已联通的子树是否存在不等关系
        for ele in equations:
        	if ele[1] == '!':
        		node_1 = ord(ele[0]) - ord('a')
        		node_2 = ord(ele[3]) - ord('a')
        		if helper_uf.connected(node_1, node_2):
        			return False

        return True

        