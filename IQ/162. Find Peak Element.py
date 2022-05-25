162. Find Peak Element




# bisection
# climbing the mountain
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        def get(i):
            nonlocal n, nums
            if i == -1 or i == n:
                return float("-inf")
            return nums[i]


        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2

            if get(mid - 1) < get(mid) > get(mid + 1):
                return mid

            if get(mid + 1) > get(mid):
                left = mid + 1

            elif get(mid - 1) > get(mid):
                right = mid

        return left 