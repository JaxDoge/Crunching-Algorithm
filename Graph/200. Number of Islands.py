200. Number of Islands

# 在一些题解中，可能会把「已遍历过的陆地格子」标记为和海洋格子一样的 0，美其名曰「陆地沉没方法」，
# 即遍历完一个陆地格子就让陆地「沉没」为海洋。这种方法看似很巧妙，但实际上有很大隐患，
# 因为这样我们就无法区分「海洋格子」和「已遍历过的陆地格子」了。如果题目更复杂一点，这很容易出 bug。


class UF:
	def __init__(self, number):
		self.count = number
		self.parent = [i for i in range(number)]
		self.size = [1] * number

	def find(self, node):
		while self.parent[node] != node:
			self.parent[node] = self.parent[self.parent[node]]
			node = self.parent[node]
		return node

	def union(self, p, q):
		rootP = self.find(p)
		rootQ = self.find(q)
		if rootP == rootQ: return

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



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    	if not grid: return 0

    	rows, columns = len(grid), len(grid[0])
    	directions = [(1,0),(-1,0),(0,1),(0,-1)]

    	helper_uf = UF(rows*columns)

    	for row in range(rows):
    		for col in range(columns):
    			if grid[row][col] == '1':
    				for dx, dy in directions:
    					newR, newC = row+dx, col+dy
    					if 0<=newR<rows and 0<=newC<columns and grid[newR][newC] == '1':
    						helper_uf.union(row*columns+col,newR*columns+newC)

        islandsDict = dict()
    	for node in helper_uf.parent:
    		island = helper_uf.find(node)
    		if grid[island//columns][island % columns] == '1' and island not in islandsDict:
    			islandsDict[island] = None

    	res = len(islandsDict)
    	return res


# DFS ，增加标记矩阵

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    	if not grid: return 0

    	rows, columns = len(grid), len(grid[0])
    	directions = [(1,0),(-1,0),(0,1),(0,-1)]  
    	import copy  	
    	flag_matrix = copy.deepcopy(grid)

    	def dfsSearch(row, col):
    		nonlocal flag_matrix
    		if not 0<=row<rows or not 0<=col<columns or flag_matrix[row][col] != '1':
    			return
    		flag_matrix[row][col] = '2'  # 搜索中的 cell 标记改为 2，避免回头路
    		for dx, dy in directions:
    			newR, newC = row+dx, col+dy
    			dfsSearch(newR, newC)

    		

    	res = 0
    	for row in range(rows):
    		for col in range(columns):
    			if flag_matrix[row][col] == '1':
    				res += 1
    				dfsSearch(row, col)

    	return res

# BFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    	if not grid: return 0

    	rows, columns = len(grid), len(grid[0])
    	directions = [(1,0),(-1,0),(0,1),(0,-1)]  
    	import copy  	
    	flag_matrix = copy.deepcopy(grid)
    	import collections
    	helper_queue = collections.deque()

    	islandNum = 0

    	def validCord(grid,row,col):
    		nonlocal rows, columns
    		return 0<=row<rows and 0<=col<columns and grid[row][col] == '1'

    	for row in range(rows):
    		for col in range(columns):
    			if flag_matrix[row][col] == '1':
    				islandNum += 1
    				helper_queue.append((row,col))
    				flag_matrix[row][col] = '2'
    				while helper_queue:
    					popR, popC = helper_queue.popleft()
    					for dx, dy in directions:
    						newR = popR + dx
    						newC = popC + dy
    						if validCord(flag_matrix, newR, newC):
    							flag_matrix[newR][newC] = '2'
    							helper_queue.append((newR,newC))

    	return islandNum
