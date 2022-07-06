剑指 Offer 21. 调整数组顺序使奇数位于偶数前面



# fast and slow pointers
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = r = 0

        while r < n:
            if nums[r] % 2 == 1:
                # change the number position
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        return nums