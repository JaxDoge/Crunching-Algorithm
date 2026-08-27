1665. Minimum Initial Energy to Finish Tasks

# Greedy
# Always deal with the task with larger buffer

class Solution:
	def minimumEffort(self, tasks: List[List[int]]) -> int:
		tasks.sort(key = lambda task: task[1] - task[0], reverse = True)

		# the energy we need
		res = 0

		# the remain energy we have before execute next task
		remain = 0

		for actual, minimum in tasks:
			# Check if current remain enery is enough for initial this task
			if remain < minimum:
				# replenish energy to minimum
				res += minimum - remain

			# after exectution, the remain is
			# No replenish, enough to pass minimum, so subtruct the actual energy
			# With replenish the remain is equal to minimum
			remain = max(remain - actual, minimum - actual)

		return res
