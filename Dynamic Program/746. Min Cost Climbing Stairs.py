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
