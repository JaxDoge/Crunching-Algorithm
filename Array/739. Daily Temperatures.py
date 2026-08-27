739. Daily Temperatures


# 往栈里压索引，索引的差值即是间距
class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		length = len(temperatures)
		res = [0] * length
		help_stack = []
		
		for i in range(length-1,-1,-1):
			while help_stack and temperatures[help_stack[-1]] <= temperatures[i]:
				help_stack.pop()
			if help_stack:
				res[i] = help_stack[-1] - i
			help_stack.append(i)
		return res



class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		n = len(temperatures)
		mono_stack = []
		ans = [0] * n

		for idx, temp in enumerate(temperatures):
			if not mono_stack or mono_stack[-1][1] >= temp:
				mono_stack.append((idx, temp))
			else:
				while mono_stack and mono_stack[-1][1] < temp:
					pop = mono_stack.pop()
					ans[pop[0]] = idx - pop[0]
				mono_stack.append((idx, temp))

		return ans