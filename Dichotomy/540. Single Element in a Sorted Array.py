540. Single Element in a Sorted Array




class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n < 2:
            return nums[0]

        l = 0
        r = n

        while l < r:
            mid = l + (r - l) // 2

            if mid == 0:
                if nums[0] != nums[1]: return nums[0]
            elif mid == n - 1:
                if nums[n - 1] != nums[n - 2]: return nums[n - 1]

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif nums[mid] == nums[mid - 1]:
                if (r - l - 1) % 2 == 0:  # Even pairs number
                    r = mid - 1
                else:
                    l = mid + 1

            elif nums[mid] == nums[mid + 1]:
                if (r - l - 1) % 2 == 0:
                    l = mid + 1
                else:
                    r = mid - 1

        return nums[l]
