343. Integer Break



# If an optimal product contains a factor f >= 4, then you can replace it with factors 2 and f-2 without losing optimality, as 2*(f-2) = 2f-4 >= f. So you never need a factor greater than or equal to 4, meaning you only need factors 1, 2 and 3 (and 1 is of course wasteful and you'd only use it for n=2 and n=3, where it's needed).

# For the rest I agree, 3*3 is simply better than 2*2*2, so you'd never use 2 more than twice.
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        quotient, remainder = n // 3, n % 3

        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 2 * 2
        elif remainder == 2:
            return 3 ** quotient * 2


# DP
# dp[0] == dp[1] == 0
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[n]