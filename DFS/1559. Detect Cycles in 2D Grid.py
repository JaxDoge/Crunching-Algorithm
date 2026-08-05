1559. Detect Cycles in 2D Grid

class Solution:
	def containsCycle(self, grid: List[List[str]]) -> bool:
		rows = len(grid)
		cols = len(grid[0])

		visited = [[False] * cols for _ in range(rows)]

		def nextNeighbor(row, col):
			for nr, nc in [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]:
				if 0<=nr<rows and 0<=nc<cols:
					yield nr, nc

		def dfs(row, col, pr, pc):

			visited[row][col] = True

			for nr, nc in nextNeighbor(row, col):
				if grid[nr][nc] != grid[row][col]:
					continue

				if nr == pr and nc == pc:
					continue

				if visited[nr][nc]:
					return True

				if dfs(nr, nc, row, col):
					return True

			return False


		for r in range(rows):
			for c in range(cols):
				if not visited[r][c]:
					if dfs(r, c, -1, -1):
						return True

		return False





		