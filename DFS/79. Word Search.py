79. Word Search


class Solution:
	def exist(self, board: list[list[str]], word: str) -> bool:
		seen = set()
		m, n = len(board), len(board[0])
		word_len = len(word)
		res = False

		def neighbor(r, c):
			for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
				if 0<=nr<m and 0<=nc<n:
					yield nr, nc

		def dfs(row, col, w_idx):
			nonlocal res
			if board[row][col] != word[w_idx] or (row, col) in seen:
				return
			
			if w_idx == word_len - 1:
				res = True
				return
			
			seen.add((row, col))
			
			for nr, nc in neighbor(row, col):
				dfs(nr, nc, w_idx + 1)
				if res:
					break
			
			seen.remove(((row, col)))
		
		for r in range(m):
			for c in range(n):
				dfs(r, c, 0)
				if res:
					return res





