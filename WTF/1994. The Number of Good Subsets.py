1994. The Number of Good Subsets


# Brainteasing
# DP
# https://leetcode.cn/problems/the-number-of-good-subsets/solution/hao-zi-ji-de-shu-mu-by-leetcode-solution-ky65/
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10**9 + 7

        freq = [0] * (31)
        for num in nums:
            freq[num] += 1

        # status compress
        # dp[mask] is the number of good subset that picked the prime combination "mask"
        # mask is one of the possible prime number combination
        # the length of dp is the number of all combinations
        dp = [0] * (1 << len(primes))
        # base case, the count of 1's combination
        dp[0] = pow(2, freq[1], mod)

        # go through the freq list
        for num, cnt in enumerate(freq):
            if num == 0 or num == 1:
                continue
            if cnt == 0:
                continue

            # check if the num has only distinct prime factors
            subset, target = 0, num
            flag = True
            for idx, pri in enumerate(primes):
                if target % (pri * pri) == 0:
                    flag = False
                    break

                # find a prime factor, update subset
                if target % pri == 0:
                    subset |= (1 << idx)

            if not flag:
                continue

            # update dp table, reverse order, dp[0] should be untouched
            for mask in range(len(dp) - 1, 0, -1):
                # check if subset is covered by mask, otherwise skip the impossible case
                if (mask & subset) == subset:
                    dp[mask] = (dp[mask] + dp[mask ^ subset] * cnt) % mod


        ans = sum(dp[1:]) % mod
        return ans
