38. Count and Say


class Solution:
	def countAndSay(self, n: int) -> str:
		if n == 1:
			return '1'

		input_string = self.countAndSay(n-1)
		n = len(input_string)
		res = []
		counter = 0

		for i in range(n):
			cur_num = input_string[i]
			counter += 1
			if i < n - 1:
				# compare with next index
				if cur_num == input_string[i+1]:
					i += 1
					continue
				else:
					# record the counter and cur_num
					res.extend([str(counter), cur_num])
					counter = 0
			else:
				res.extend([str(counter), cur_num])

		return ''.join(res)


class Solution:
	def countAndSay(self, n: int) -> str:
		if n == 1:
			return '1'
		
		pre_out = self.countAndSay(n - 1)
		count = 0
		res = []
		for i in range(len(pre_out)):
			if i > 0 and pre_out[i] != pre_out[i - 1]:
				res.append(str(count) + pre_out[i - 1])
				count = 1
			else:
				count += 1

		res.append(str(count) + pre_out[-1])

		return "".join(res)

