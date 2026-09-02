2528. Maximize the Minimum Powered City


# Binary search: For a given power level x, can we ensure every city has at least x power providers
# Difference array: stations[i] can affect a range, add a new power station will affect a range as well. So we need to use difference array to optimize the array update
# Greedy algorithm: Note that from left to right the first city need more power means we only need to put the new station in i + r, it will cover the range [i,i+2r]
class Solution:
	def maxPower(self, stations: List[int], r: int, k: int) -> int:
		# Note that we never need to maintain the real city power list
		# Because we can calculate each city current power supply on fly

		n = len(stations)

		# The initial difference array
		# Why n + 1, that can help us avoid the special treatment if end >= n, so we can always update diff[n] like a trash bin
		diff_o = [0] * (n + 1)

		for i in range(n):
			left = max(0, i - r)
			right = min(n, i + r + 1)
			diff_o[left] += stations[i]
			diff_o[right] -= stations[i]

		def check(value):
			diff = diff_o[:]
			total = 0
			remaining = k

			# Compare city i with threshold
			for i in range(n):
				total += diff[i]
				if total < value:
					add = value - total
					if remaining < add:
						return False
					remaining -= add
					end = min(n, i + 2 * r + 1)
					diff[end] -= add
					total += add

			return True

		low, high = min(stations), sum(stations) + k

		# Find the highest value can pass the check

		while low <= high:
			mid = (high + low) // 2

			if check(mid):
				low = mid + 1
			else:
				high = mid - 1

		return high