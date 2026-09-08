283. Move Zeroes

# 类似移除某个元素，把所有的非零的数都移动到前半部分，再把后半部分全部赋值为 0
class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		if len(nums) == 0:
			return
		length = len(nums)
		left = right = 0
		while right < length:
			if nums[right] != 0:
				nums[left] = nums[right]
				left += 1
			right += 1

		for index in range(left,length):
			nums[index] = 0
		return


# Swap
class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		p1 = p2 = 0

		while True:
			while p1 < n and nums[p1] != 0:
				p1 += 1
			
			p2 = max(p1, p2)

			while p2 < n and nums[p2] == 0:
				p2 += 1

			if p1 >= n or p2 >= n:
				break
				
			nums[p1], nums[p2] = nums[p2], nums[p1]