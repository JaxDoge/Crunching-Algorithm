#  Divide and conquer
#  Add memo to reduce duplicated task
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        op_set = {'+', '-', '*'}
        memo = dict()

        def calculation(list_exp: str, start, end):
            # check memo
            if list_exp[start:end] in memo.keys():
                return memo[list_exp[start:end]]
            # base case
            if list_exp[start:end].isdigit():  # return the only number left in range
                return [int(list_exp[start:end])]

            res = list()
            for i in range(start, end):
                char = list_exp[i]
                if char in op_set:
                    left_p = calculation(list_exp, start, i)
                    right_p = calculation(list_exp, i+1, end)

                    for a in left_p:
                        for b in right_p:
                            if char == '+':
                                res.append(a + b)
                            elif char == '-':
                                res.append(a - b)
                            elif char == '*':
                                res.append(a * b)
            memo[list_exp[start:end]] = res
            return res

        return calculation(expression, 0, len(expression))

