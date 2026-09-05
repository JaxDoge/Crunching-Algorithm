37. Sudoku Solver

class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""

		rows = [set() for _ in range(9)]
		cols = [set() for _ in range(9)]
		boxes = [set() for _ in range(9)]

		empty = []

		for i in range(9):
			for j in range(9):
				val = board[i][j]
				if val != '.':
					rows[i].add(val)
					cols[j].add(val)
					boxes[(i // 3) * 3 + j // 3].add(val)
				else:
					empty.append((i, j))

		def backtrack(idx):
			if idx == len(empty):
				return True

			# current cell
			r, c = empty[idx]
			box_id = (r//3)*3 + c//3

			for cand in '123456789':
				if (
					cand in rows[r] or 
					cand in cols[c] or 
					cand in boxes[box_id]
					):
					continue

				# Fill this cell
				board[r][c] = cand
				rows[r].add(cand)
				cols[c].add(cand)
				boxes[box_id].add(cand)

				if backtrack(idx+1):
					return True

				# pop out
				board[r][c] = '.'
				rows[r].remove(cand)
				cols[c].remove(cand)
				boxes[box_id].remove(cand)

			return False

		backtrack(0)			



