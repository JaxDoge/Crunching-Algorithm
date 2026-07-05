class Solution:
	def calculate(self, s: str) -> int:
		s = deque(list(s))
		
		# Calculate each bracket pair
		def sub_calculator(input_deque):
			num = 0 
			# Post-processing stack. It only has positive or negative numbers
			stack_list = []
			sign = '+'

			while len(input_deque) > 0:
				c = input_deque.popleft()
				# The ifs order is important
				# left bracket start the recursion, right bracket return the result number
				if c == '(':
					num = sub_calculator(input_deque)

				# convert string to numeric
				if c.isdigit():
					num = num*10 + int(c)

				# find sign character or the end of expression (end of current number, including trailing spaces)
				if (not c.isdigit() and c != ' ') or len(input_deque) == 0:
					if sign == '+':
						stack_list.append(num)
					elif sign == '-':
						stack_list.append(-num)
					elif sign == '*':
						stack_list[-1] = stack_list[-1] * num  
					elif sign == '/':
						stack_list[-1] = int(stack_list[-1] / num)
					#  finish sub process
					num = 0
					sign = c 

				# right bracket is the flag of end recursion
				if c == ')':
					break               

			return sum(stack_list)

		return sub_calculator(s)

