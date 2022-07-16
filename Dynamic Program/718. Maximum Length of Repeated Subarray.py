718. Maximum Length of Repeated Subarray



# DP, no doubt
# dp[i][j] is the longest repeated subarray in nums1[:i] and nums[:j], meanwhile the i, j is then end points 
# of the repeated subarray
# If nums[i] == nums[j] then dp[i][j] = 1 + dp[i -1][j - 1]
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])

        return ans
