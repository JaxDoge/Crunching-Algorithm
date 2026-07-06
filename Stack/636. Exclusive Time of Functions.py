636. Exclusive Time of Functions




# 1. For an empty stack, push a Function object for starting
# 2. if the log is a function starting, update the Function object on the top - process_time = start_at_new_func - start_at_top_func
# 3. if the log is a function ending, update the final result with the end-start. Moreover, if there is a Function object on the top, update the start_at
# Note that the end_at timestamp point to the end_at + 1 time index

class Function:
	def __init__(self, func_id, start_at):
		self.func_id = func_id
		self.start_at = start_at
		self.process_time = 0

class Solution:
	def _split_log(self, log):
		log_list = log.split(':')
		return int(log_list[0]), log_list[1], int(log_list[2])

	def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
		res = [0] * n
		stack = []

		for log in logs:
			func_id, action, timestamp = self._split_log(log)

			if action == 'start':
				new_func = Function(func_id, timestamp)

				if stack:
					recent_func = stack[-1]
					recent_func.process_time += new_func.start_at - recent_func.start_at
				stack.append(new_func)

			else:
				paired_func = stack.pop()
				processing_time = paired_func.process_time + (timestamp + 1 - paired_func.start_at)
				res[func_id] += processing_time

				if stack:
					stack[-1].start_at = timestamp + 1

		return res


		