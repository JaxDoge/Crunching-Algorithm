2376. Count Special Integers


# Best entry level digit DP
# Assume n is 489, now the problem is for a three digit slot _ _ _, what we should put in current position
# We use mask number to mark what digit numbers are used before
# Note if we leading 0, then we can still use 0 later

from functools import cache
class Solution:
	def countSpecialNumbers(self, n: int) -> int:
		# The n tells us the possible limit of each position
		# And how many position we need to consider
		digits = str(n)
		m = len(digits)

		# pos: which digit we're currently filling, start from the most significant one
		# mask: which digits have already appeared
		# tight: whether our prefix is exactly equal to n's prefix
		# started: whether we've placed the first non-leading-zero digit yet
		@cache
		def dfs(pos, mask, tight, started):

			# Finish constructing, check if the number is 00...0
			if pos == m:
				return 1 if started else 0

			# Check the limitation of current position
			limit = int(digits[pos]) if tight else 9

			ans = 0

			for digit in range(limit + 1):
				# Set next position tight
				next_tight = tight and (digit == limit)

				# If we still padding 0 in prefix, we can skip it, no mask change
				if digit == 0 and not started:
					ans += dfs(pos + 1, mask, next_tight, started)
					continue

				# If digit already used
				if mask & 1 << digit:
					continue

				ans += dfs(pos + 1, mask | 1 << digit, next_tight, True)

			return ans

		# The most signifcant position is always tighted
		return dfs(0, 0, True, False)


