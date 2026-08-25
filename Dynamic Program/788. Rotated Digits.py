788. Rotated Digits

# Digit DP

from functools import cache
class Solution:
	def rotatedDigits(self, n: int) -> int:
		good_single = {0, 1, 8}
		good_double = {2, 5, 6, 9}
		good_digits = good_single | good_double

		digits = str(n)
		m = len(digits)

		@cache
		def dfs(pos, is_good, started, tight):
			# Base case, not 000...000 is not counted (not started yet)
			if pos == m:
				return int(is_good and started)

			limit = int(digits[pos]) if tight else 9

			res = 0

			for _, digit in enumerate(good_digits):
				if digit > limit:
					continue

				next_tight = tight and digit == limit

				# case 1, still padding leading 0s
				if not started and digit == 0:
					res += dfs(pos + 1, is_good, started, next_tight)


				else:
					res += dfs(pos + 1, is_good or digit in good_double, True, next_tight)

			return res

		return dfs(0, False, False, True)

