1648. Sell Diminishing-Valued Colored Balls

# Binary search
# We need to sell (decrease) the ball from the largest stock
MOD = 10 ** 9 + 7
class Solution:
	def maxProfit(self, inventory: List[int], orders: int) -> int:
		inventory.sort(reverse = True)
		high = max(inventory)
		low = 0

		def check(target):
			selled = 0
			profit = 0
			for stock in inventory:
				if stock > target:
					single_selled = stock - target
					selled += single_selled
					profit = (((stock + (target + 1)) * single_selled // 2) % MOD + profit % MOD) % MOD
				else:
					break

			if selled > orders:
				return False, selled, profit

			return True, selled, profit

		while low <= high:
			mid = (low + high) // 2

			check_output, _, _ = check(mid)

			# If we sell less or equal to orders
			if check_output:
				high = mid - 1
			# If we sell to much
			else:
				low = mid + 1

		# low is what we looking for
		_, selled, profit = check(low)
		if selled < orders:
			profit = ((low % MOD * (orders - selled) % MOD) % MOD + profit % MOD) % MOD

		return profit