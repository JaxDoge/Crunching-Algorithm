1493. Longest Subarray of 1's After Deleting One Element

# always maintain the biggest window
# subtract the remove_cnt from the final result

class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		n = len(nums)
		pl = pr = 0
		k = 1

		while pr < n:
			if nums[pr] == 0:
				k -= 1

			pr += 1

			# only slide the window if we covered more than one ZERO
			if k < 0:
				# if we move out a ZERO
				if nums[pl] == 0:
					k += 1
				pl += 1



		return pr - pl - 1