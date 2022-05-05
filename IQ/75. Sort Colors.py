75. Sort Colors


# Double pointers
# I'll call it triple pointers
# Detail-Oriented!
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0 = 0 # the next position of next zero
        p2 = n - 1 # the next position of next two

        for i in range(n):
            if i > p2:
                break

            while i <= p2 and nums[i] == 2:
                # continuously change change the value at i and p2, until there is no two at the left of i
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1

            if nums[i] == 0:
                # change the value at i and p0
                # p0 will always point to the true next zero position or equals to i
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1

        return