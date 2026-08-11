3336. Find the Number of Subsequences With Equal GCD

# Note that matrix value in dp[n] only rely on value in matrix dp[n-1], we can diminish this dimension
# j is the (assumably) gcd of seq1 and k is gcd of seq2
# For a given prefix `num` and `num - 1`
# ndp[j][k]+=dp[j][k]
# ndp[gcd(j,nums[i])][k]+=dp[j][k] (put num to the seq1)
# ndp[j][gcd(k,nums[i])]+=dp[j][k] (put num to the seq2)
# Initially, before processing any elements, both subsequences are empty. We define the GCD of an empty subsequence as 0, so the first dp[0][0] = 1
# j, k is the possible GCD less than max(nums)

class Solution:
	def subsequencePairCount(self, nums: list[int]) -> int:
		MOD = 1e9+7
		m = max(nums)
		dp = [[0] * (m + 1) for _ in range(m + 1)]
		dp[0][0] = 1

		for num in nums:

			ndp = [[0] * (m + 1) for _ in range(m + 1)]

			# enumerate all possible j, k combination, most of them should be invalid
			for j in range(m + 1):
				ngcd_1 = math.gcd(j, num)

				for k in range(m + 1):
					val = dp[j][k]

					# Check if the j, k are valid
					if val == 0:
						continue

					ngcd_2 = math.gcd(k, num)

					# Update
					ndp[j][k] = (ndp[j][k] + val) % MOD
					ndp[ngcd_1][k] = (ndp[ngcd_1][k] + val) % MOD
					ndp[j][ngcd_2] = (ndp[j][ngcd_2] + val) % MOD

			dp = ndp

		# subsequences are non-empty, so dp[0][0] is ruled out
		res = 0
		for i in range(1, m + 1):
			res = (res + dp[i][i]) % MOD

		return int(res)

