class Solution:
    def __init__(self):
        """
        The number of left parentheses should be equal to the number of right ones.
        At any given time, the rest left parentheses should be always less than the rest of right one.
        """
        self.res = list()

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        one_comb = list()
        self.backtrack(n, n, one_comb)
        return self.res

    def backtrack(self, left, right, this_comb):
        if left > right:
            return
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            self.res.append("".join(this_comb.copy()))
            return

        # try to add a left parentheses into combination
        this_comb.append('(')
        self.backtrack(left-1, right, this_comb)
        this_comb.pop()

        # try to add a right parentheses into combination
        this_comb.append(')')
        self.backtrack(left, right-1, this_comb)
        this_comb.pop()




