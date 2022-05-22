153. Find Minimum in Rotated Sorted Array




class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            # minimum number on the left
            if nums[mid] < nums[right] :
                right = mid
            # minimum number on the right, or mid == left == right    
            elif nums[mid] >= nums[right]:
                left = mid + 1



        return nums[right]  # return the number at right index, because left = right + 1 = mid + 1 in the end