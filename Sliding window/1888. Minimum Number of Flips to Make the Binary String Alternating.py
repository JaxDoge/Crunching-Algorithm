1888. Minimum Number of Flips to Make the Binary String Alternating

# The substring length parity
# If even length string is alternating, then append any 1 or 0 will also be alternating (one can always do REMOVE operation to rearrange the string to be alternating)
# If odd lenght string is alternating, then we need to check the next character

class Solution:
	def minFlips(self, s: str) -> int:
		n = len(s)

		ss = s + s

		diff_0 = 0 # the mismatch against 01010...
		diff_1 = 0 # the mismatch against 10101...

		left = 0
		res = float('inf')

		for right in range(2 * n):
			pattern_0_expect = '0' if right % 2 == 0 else '1'
			pattern_1_expect = '1' if right % 2 == 0 else '0'

			if ss[right] != pattern_0_expect:
				diff_0 += 1

			if ss[right] != pattern_1_expect:
				diff_1 += 1

			# shrink the window and may reduce the mismatch
			if right - left + 1 > n:
				pattern_0_expect_left = '0' if left % 2 == 0 else '1'
				pattern_1_expect_left = '1' if left % 2 == 0 else '0'

				if ss[left] != pattern_0_expect_left:
					diff_0 -= 1
				if ss[left] != pattern_1_expect_left:
					diff_1 -= 1

				left += 1

			# We should always shrink first then check the length is valid
			# Other wise the below condition can only be meet once (first time)
			if right - left + 1 == n:
				res = min(res, diff_0, diff_1)

		return res

