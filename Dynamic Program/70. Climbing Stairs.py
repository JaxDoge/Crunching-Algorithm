70. Climbing Stairs


# Dfs; backtrack + memo
from collections import defaultdict
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        memo = defaultdict(int)

        def search(step):
            nonlocal memo
            if step == n:
                return 1

            if step > n:
                return 0

            if step in memo:
                return memo[step]

            memo[step] = search(step + 1) + search(step + 2)
            return memo[step]

        search(0)

        return memo[0]


# DP

class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(2, n+1):
            a, b = b, a + b

        return b