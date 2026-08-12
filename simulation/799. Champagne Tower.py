799. Champagne Tower


class Solution:
	def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
		# We have maximum 100 level glasses, and add one more level as the floor
		T = [[0] * row for row in range(1, 102)]

		T[0][0] = poured

		# Start simulation
		for i in range(query_row + 1):
			for j in range(i + 1):
				out = T[i][j] - 1
				if out > 0:
					child_out = out / 2
					T[i+1][j] += child_out
					T[i+1][j+1] += child_out

		# The glass can hold up to 1 cup of champagne
		return min(1, T[query_row][query_glass])