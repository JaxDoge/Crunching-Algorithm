59. Spiral Matrix II



class Solution:
	def generateMatrix(self, n: int) -> list[list[int]]:
		res = [[0] * n for _ in range(n)]
		directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

		cur_dir_idx = 0
		cur_dir = directions[cur_dir_idx]
		row, col = 0, 0
		for i in range(1, n ** 2 + 1):
			res[row][col] = i
			if (
				not (0 <= row + cur_dir[0] < n) or
				not (0 <= col + cur_dir[1] < n) or
				res[row + cur_dir[0]][col + cur_dir[1]]
			):
				cur_dir_idx = (cur_dir_idx + 1) % len(directions)
				cur_dir = directions[cur_dir_idx]
			
			row += cur_dir[0]
			col += cur_dir[1]
		
		return res
		
