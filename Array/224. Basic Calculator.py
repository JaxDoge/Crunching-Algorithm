class Solution:
    def calculate(self, s: str) -> int:
        from collections import deque
        s = deque(list(s))
        
        def sub_calculator(input_deque):
            num = 0 
            stack_list = []
            sign = '+'

            while len(input_deque) > 0:
                c = input_deque.popleft()
                #  left bracket start the recursion, right bracket return the result number
                if c == '(':
                    num = sub_calculator(input_deque)

                #  convert string to numeric
                if c.isdigit():
                    num = num*10 + int(c)

                #  find sign character or the end of expression
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
                #  right bracked is the flag of end recursion
                if c == ')':
                    break               

            return sum(stack_list)

        return sub_calculator(s)

