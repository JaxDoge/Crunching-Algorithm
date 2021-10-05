704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left: int, right: int):
            nonlocal nums, target
            # 移动双指针一定要考虑这个溢出的问题
            if left > right: return -1
            if left == right:
                if nums[left] == target:
                    return left
                else:
                    return -1
			# 计算 mid 时需要防止溢出，代码中 left + (right - left) / 2 就和 (left + right) / 2 的结果相同，
			# 但是有效防止了 left 和 right 太大直接相加导致溢出。
            mid_index = left + (right - left) // 2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                return binarySearch(left,mid_index-1)
            elif nums[mid_index] < target:
                return binarySearch(mid_index+1,right)
        return binarySearch(0, len(nums)-1)                