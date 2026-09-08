3312. Sorted GCD Pair Queries

# Inclusion-Exclusion Principle + Prefix Sum + Binary Search
# We don't need to enumerate all pairs and compute their GCD. Infeasible
# We only need to know for a given GCD g, how many pairs do we have
# Note that the max value of g is limited (5 * 10^4). Thus we can use an array as hash table

class Solution:
	def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
		mx = max(nums)

		# Counter for each number
		freq = [0] * (mx + 1)
		for num in nums:
			freq[num] += 1

		# gcd table
		gcd_count = [0] * (mx + 1)

		# Start from the largest possible gcd
		for g in range(mx, 0, -1):

			divisible = 0
			# divisor seive. Try g * 1, g * 2...
			for multiple in range(g, mx + 1, g):
				divisible += freq[multiple]

			# Use combination formular to get the pairs number
			pairs_cnt = divisible * (divisible - 1) // 2

			# Note g is the least CD, not always GCD
			# we need to remove the pairs count whose GCD is 2g, 3g, 4g, ...
			for multiple in range(g * 2, mx + 1, g):
				pairs_cnt -= gcd_count[multiple]

			# Then we get the real gcd_count[g]
			gcd_count[g] = pairs_cnt

		# Use prefix array to quickly query given index value
		# prefix[g] = number of pairs whose GCD <= g
		prefix = [0] * (mx + 1)

		for i in range(1, mx + 1):
			prefix[i] = prefix[i - 1] + gcd_count[i]
			
		# query is a 0-index in the conceptual sorted gcdPairs array.
		# Find first g such that prefix[g] > query.
		return [bisect(prefix, q) for q in queries]



		