# TikTok - 2. Real Programmer Game

# Similar to Leetcode 1155

class Solution:
	def RealProgrammerGame(self, N: int, M: int, K: int):
		max_dmg = M * K

		# bad case: K swing cannot kill monster
		if max_dmg < N:
			return 0 

		dp_table = [[0] * (max_dmg + 1) for _ in range(K + 1)]

		# base case
		for i in range(K + 1):
			dp_table[i][0] = 1


		for i in range(1, K + 1):
			for j in range(1, max_dmg + 1):
				for x in range(0, M + 1):
					if j - x >= 0:
						dp_table[i][j] = dp_table[i][j] + dp_table[i - 1][j - x]

		return sum(dp_table[K][N:(max_dmg + 2)]) / sum(dp_table[K])



sltin = Solution()

print(sltin.RealProgrammerGame(99, 66, 33))


