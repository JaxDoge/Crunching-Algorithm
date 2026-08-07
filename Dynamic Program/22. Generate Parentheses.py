22. Generate Parentheses

# Every valid parentheses string has a uniquely matched pair around its first opening parenthesis: ( leftpart ) rightpart
# For a given n, suppose the leftpart contain j parentheses so the right part must contain n - j - 1 parentheses
# Note that 0 < j <= n - 1
class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		dp = [[] for _ in range(n + 1)]

		dp[0] = [""]

		for pairs in range(1, n + 1):
			for left_part in range(pairs):
				right_part = pairs - left_part - 1

				for left in dp[left_part]:
					for right in dp[right_part]:
						dp[pairs].append('(' + left + ')' + right)

		return dp[n]