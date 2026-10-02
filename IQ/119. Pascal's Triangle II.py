119. Pascals Triangle II


class Solution:
	def getRow(self, rowIndex: int) -> list[int]:
		row = [1] * (rowIndex + 1)
		if rowIndex < 2:
			return row
		
		for i in range(2, rowIndex + 1):
			for j in range(i - 1, 0, -1):
				row[j] = row[j] + row[j - 1]

		return row
