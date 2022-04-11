31. Next Permutation


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # scan from right to left, find the first decsending neighbor
        right = n - 1
        while right > 0:
            if nums[right] <= nums[right-1]:
                right -= 1
            else:
                left = right - 1
                break

        if right == 0:
            nums.sort()
        else:
            # find the element just larger than nums[left]
            # remember the nums[left+1:n] is already in descending order
            right = n - 1
            while right > left and nums[left] >= nums[right]:
                right -= 1

            nums[left], nums[right] = nums[right], nums[left]

            # the permutation of nums[left+1:n] must be in descending order. 
            # reverse it
            left, right = left + 1, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


