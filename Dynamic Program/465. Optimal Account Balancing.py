465. Optimal Account Balancing

# If sum(mask) == 0:
#     dp[mask] = max(dp[mask without one person]) + 1
# else:
#     dp[mask] = max(dp[mask without one person])

class Solution:
	def minTransfers(self, transactions: List[List[int]]) -> int:
		# Calculate the final balance of each person
		balance_map = defaultdict(int)
		for fr, to, amount in transactions:
			balance_map[fr] -= amount
			balance_map[to] += amount

		# Only the non-zero balance person need to attend the transactions
		# We need to split the balance list in to as many zero sum subgroup as possible
		balance_list = [amount for amount in balance_map.values() if amount]
		n = len(balance_list)

		# DFS memo
		memo = [-1] * (1 << n)
		memo[0] = 0

		def dfs(mask):
			if memo[mask] != -1:
				return memo[mask]

			this_balance_sum = 0
			this_res = 0

			# Remove one person in the mask each time
			# Bitwise & can do the filter
			for i in range(n):
				cur_bit = 1 << i
				if cur_bit & mask:
					# this balance only calculate the person in the mask as well 
					this_balance_sum += balance_list[i]
					this_res = max(this_res, dfs(mask ^ cur_bit))

			this_res = this_res + (this_balance_sum == 0)
			memo[mask] = this_res
			return this_res

		return n - dfs((1 << n) - 1)

			