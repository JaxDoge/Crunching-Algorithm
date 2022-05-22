150. Evaluate Reverse Polish Notation



# stack
class Solution:
    def __init__(self):
        self.operators = {"+","-","*","/"}

    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in range(n):
            if tokens[i] not in self.operators:
                stack.append(int(tokens[i]))
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                if tokens[i] == "+":
                    tmp = lhs + rhs
                elif tokens[i] == "-":
                    tmp = lhs - rhs
                elif tokens[i] == "*":
                    tmp = lhs * rhs
                elif tokens[i] == "/":
                    tmp = int(lhs / rhs)
                stack.append(tmp) 

        return stack[0]
