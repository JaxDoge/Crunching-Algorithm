# Mapping
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # note that the value start from 1
        n = len(nums)
        dup = 0
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                dup = abs(nums[i])
            else:
                nums[idx] *= -1

        missing = 0
        for i in range(n):
            if nums[i] > 0:
                # the value equals to the corresponding index add one
                missing = i + 1

        return [dup, missing]
