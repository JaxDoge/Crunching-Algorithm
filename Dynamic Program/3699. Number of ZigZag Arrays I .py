3699. Number of ZigZag Arrays I

# DP + prefix sum optimization
# up[i], and down[i] represent the possible array number that the end value is i and direction is up or down. For a given m
# Note the state for m is solely depended on m - 1 so we can compress the dp table by one dimension

class Solution:
	def zigZagArrays(self, n: int, l: int, r: int) -> int:
		MOD = 1e9 + 7 # it's float

		# Essentially, we have m = r - l + 1 possible selection for any position, so we can map the range to [0, m)
		m = r - l + 1

		up = [0] * m
		down = [0] * m

		# Note that we initial the dp table from n = 2
		# Because n = 1 is meaningless (no up or down)
		# When n = 2, the up[i] is directly related to i
		for i in range(m):
			up[i] = i
			down[i] = m - 1 - i

		for _ in range(3, n + 1):
			new_up = [0] * m
			new_down = [0] * m

			# new_up[x] = sum(down[y]) for y < x
			prefix = 0
			for i in range(m):
				new_up[i] = prefix
				prefix = (prefix + down[i]) % MOD

			# new_down[x] = sum(up[y]) for y > x
			suffix = 0
			for i in range(m - 1, -1, -1):
				new_down[i] = suffix
				suffix = (suffix + up[i]) % MOD

			up = new_up
			down = new_down

		return int((sum(up) % MOD + sum(down) % MOD) % MOD)


# Notice the symmetry

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        # dp[x] = number of length-2 arrays ending at x
        # whose last direction is UP.
        #
        # Previous value can be any value < x.
        dp = [x for x in range(m)]

        for _ in range(2, n):
            new_dp = [0] * m

            suffix = 0

            for x in range(m):
                new_dp[x] = suffix

                # Add mirrored element for the next x
                suffix = (suffix + dp[m - 1 - x]) % MOD

            dp = new_dp

        # UP and DOWN have the same total count by symmetry
        return 2 * sum(dp) % MOD