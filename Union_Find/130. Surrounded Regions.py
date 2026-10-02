130. Surrounded Regions


# 方法一：并查集，杀鸡用牛刀，给所有与边缘联通的 o 增加一个公共 root，再把所有没有该祖先节点的 o 换成 x.
# 首先要解决的是，根据我们的实现，Union-Find 底层用的是一维数组，构造函数需要传入这个数组的大小，而题目给的是一个二维棋盘。
# 这个很简单，二维坐标 (x,y) 可以转换成 x * n + y 这个数（m 是棋盘的行数，n 是棋盘的列数）。敲黑板，这是将二维坐标映射到一维的常用技巧。
# 其次，我们之前描述的「祖师爷」是虚构的，需要给他老人家留个位置。索引 [0.. m*n-1] 都是棋盘内坐标的一维映射，那就让这个虚拟的 dummy 节点占据索引 m * n 好了。

class Solution:
	def solve(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""


# Marker escape O first then marker the rest O
class Solution:
	def solve(self, board: list[list[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		m = len(board)
		n = len(board[0])

		def neighbors(row, col):
			for n_row, n_col in [[row + 1, col], [row, col + 1], [row - 1, col], [row, col - 1]]:
				if 0<=n_row<m and 0<=n_col<n:
					yield n_row, n_col

		def markEscape(row, col):
			if board[row][col] == 'X' or board[row][col] == 'OE':
				return
			if board[row][col] == 'O':
				board[row][col] = 'OE'
			
			for n_row, n_col in neighbors(row, col):
				markEscape(n_row, n_col)

		# The escape Os must have at least one edge O
		# So we can search from four edges.
		for j in range(n):
			markEscape(0, j)
			markEscape(m - 1, j)

		for i in range(1, m - 1):
			markEscape(i, 0)
			markEscape(i, n - 1)

		for i in range(m):
			for j in range(n):
				if board[i][j] == 'OE':
					board[i][j] = 'O'
				elif board[i][j] == 'O':
					board[i][j] = 'X'