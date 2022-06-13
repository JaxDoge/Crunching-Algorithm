剑指 Offer 11. 旋转数组的最小数字

# Same as https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1

        return numbers[left]