152. Maximum Product Subarray


# kadane's algorithm
# Note that we need another dp table minDP to record the minimum product of subarray end with nums[i-1]
# Because nums[i] could be negative, thus it could get a largest value with the minimum values 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]

        maxDP = [nums[0]]
        minDP = [nums[0]]
        for i in range(1, n):
            maxI = max(maxDP[i - 1] * nums[i], minDP[i - 1] * nums[i], nums[i])
            minI = min(maxDP[i - 1] * nums[i], minDP[i - 1] * nums[i], nums[i])
            maxDP.append(maxI)
            minDP.append(minI)

        return max(maxDP)


# Obviously not this way
# time limitation exceeded!!
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = float("-inf")

        for i in range(n):
            cur = nums[i]
            for j in range(i, n):
                if j != i:
                    cur *= nums[j]

                res = max(res, cur)

        return res

