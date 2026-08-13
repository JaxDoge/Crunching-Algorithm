746. Min Cost Climbing Stairs


# DP
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [sum(cost)] * n
        dp[n - 1] = cost[n - 1]
        dp[n - 2] = cost[n - 2]

        for i in range(n - 3, -1, -1):
            dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])

        return min(dp[0], dp[1])



# From bottom to top
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [float('inf')] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        # we need to find the dp[n - 2] and dp[n-1]
        if n < 3:
            return min(dp[0], dp[1])

        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return min(dp[n - 2], dp[n - 1])