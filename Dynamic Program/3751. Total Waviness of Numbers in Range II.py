3751. Total Waviness of Numbers in Range II

from functools import cache
class Solution:
	def totalWaviness(self, num1: int, num2: int) -> int:
		
		# Solve [0:x]
		def solve(x):
			digits = str(x)
			n = len(digits)

			@cache
			def dfs(pos, pre2, pre1, length, tight):
				# Return two value
				# num_cnt: how many numbers can be generated from this prefix
				# wave_cnt: how many wave can we find in this state
				if pos == n:
					return 1, 0

				limit = int(digits[pos]) if tight else 9

				num_cnt = 0
				wave_cnt = 0

				for d in range(limit + 1):
					new_tight = tight and (d == limit)

					# if we are padding leading ZERO, skip it
					if length == 0 and d == 0:
						child_num_cnt, child_wave_cnt = dfs(pos + 1, pre2, pre1, length, new_tight)
						num_cnt += child_num_cnt
						wave_cnt += child_wave_cnt

					# There is less than 3 digits right now
					elif length < 2:
						child_num_cnt, child_wave_cnt = dfs(pos + 1, pre1, d, length + 1, new_tight)
						num_cnt += child_num_cnt
						wave_cnt += child_wave_cnt

					else:
						is_wave = (pre1 > pre2 and pre1 > d) or (pre1 < pre2 and pre1 < d)
						child_num_cnt, child_wave_cnt = dfs(pos + 1, pre1, d, length + 1, new_tight)
						num_cnt += child_num_cnt
						wave_cnt += child_wave_cnt + is_wave * child_num_cnt

				return num_cnt, wave_cnt
			return dfs(0, -1, -1, 0, True)[1]

		return solve(num2) - solve(num1-1)