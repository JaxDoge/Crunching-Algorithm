3946. Maximum Number of Items From Sale I

# The trick part is that only the first copy of each item meaningful
# Cause that can (potenially) contribute > 1 value.
# So the problem is a 0/1 knapsack problem afterall
# The only thing left is we can reuse the leftover budget to buy the cheapest item in the end

class Solution:
	def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
		n = len(items)

		# calculate the gain of each item in the first copy
		# it must take n^2 time
		gain = [1] * n

		for i in range(n):
			for j in range(n):
				if i != j and items[j][0] % items[i][0] == 0:
					gain[i] += 1

		cheapest_price = min(price for _, price in items)

		# 0/1 knapsack with dimension optimized
		dp = [0] * (budget + 1)

		# We don't need to consider 0 item case
		# And it can match the gain list index
		for i in range(n):
			price = items[i][1]
			# Starting from back, so that we also have data of
        	# previous computation of i-1 scenario
			for b in range(budget, price - 1, -1):
				dp[b] = max(dp[b], dp[b - price] + gain[i])

		res = 0
		for b in range(budget + 1):
			leftover = (budget - b) // cheapest_price
			res = max(res, dp[b] + leftover)

		return res
