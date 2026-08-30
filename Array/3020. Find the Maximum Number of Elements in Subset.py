3020. Find the Maximum Number of Elements in Subset


class Solution:
	def maximumLength(self, nums: List[int]) -> int:
		nums.sort()
		n = len(nums)
		select_dict = defaultdict(int)

		for num in nums:
			select_dict[num] += 1

		seen = set()
		res = 0

		i = 0
		while i < n:
			# avoid repeat
			if i > 0 and nums[i] == nums[i - 1]:
				i += 1
				continue

			# if this number have been before
			if nums[i] in seen:
				i += 1
				continue

			# Note 1 is a special case, [1], [1,1,1] are valid
			if nums[i] == 1:
				cnt = select_dict[1]
				res = max(res, cnt if cnt % 2 else cnt - 1)
				i += 1
				continue
				
			cur_num = nums[i]
			cur_length = 0

			# construct the array
			while True:
				# center element existed
				# Note that a valid subset always has odd length
				if cur_num in select_dict:
					seen.add(cur_num)
					cur_length += 1
					# have more than 1 cur_num, continue the construction
					if select_dict[cur_num] > 1:
						cur_length += 1
						cur_num *= cur_num
						continue
				else:
					cur_length -= 1
				
				break

			res = max(res, cur_length)
			i += 1

		return res







