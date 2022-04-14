35. Search Insert Position

# bisect
# find the insert position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return l