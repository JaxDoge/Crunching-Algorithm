3413. Maximum Coins From K Consecutive Bags

# i = interval where the candidate window starts

# window = [coins[i].left, coins[i].left + k - 1]

# j = first interval not completely inside window

# window_sum = sum of all completely covered intervals
# part       = contribution of interval j, if partially covered

class Solution:
	def maximumCoins(self, coins: List[List[int]], k: int) -> int:
		def slide(coins):
			n = len(coins)
			coins.sort(key = itemgetter(0))

			# Sliding window

			# Start from start point, so we scan the list from left to right
			# Initialize the window
			window_sum = 0
			res = 0
			j = 0 # track the interval index that not completely inside the window

			for i in range(n):
				right = coins[i][0] + k - 1

				while j < n and coins[j][1] <= right:
					window_sum += (coins[j][1] - coins[j][0] + 1) * coins[j][2]
					j += 1

				# Check partially covered interval
				part = 0
				if j < n and coins[j][0] <= right:
					part = (right - coins[j][0] + 1) * coins[j][2]

				res = max(res, window_sum + part)

				# Edge case, if there is no complete covered interval in the first place, window_sum will be 0 so nothing to subtract (empty window).
				# In this case i >= j
				window_sum -= (coins[i][1] - coins[i][0] + 1) * coins[i][2] if i < j else 0

				# Same edge case, j cannot lag behind i + 1 in next loop
				j = max(j, i + 1)

			return res

		forward = slide([x[:] for x in coins])

		backward = slide([
			[-r, -l, c]
			for l, r, c in coins
		])

		return max(forward, backward)




