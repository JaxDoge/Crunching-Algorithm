154. Find Minimum in Rotated Sorted Array II



class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        # Note that it is a unconventional dichotomy code
        # if your wanna find a certain value, the last element that left == right is neglected
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[left]  # or nums[right]