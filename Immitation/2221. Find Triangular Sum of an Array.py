2221. Find Triangular Sum of an Array


# Amazon intern OA
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newNum = []
            for i in range(len(nums) - 1):
                newNum.append((nums[i] + nums[i + 1]) % 10)

            nums = newNum

        return nums[0]