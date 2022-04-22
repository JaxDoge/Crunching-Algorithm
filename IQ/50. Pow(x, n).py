50. Pow(x, n)


# Quick pow
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        # convert n to positive
        revFlag = False
        if n < 0:
            revFlag = True
            n = abs(n)

        ans = self.helper(x, n, 1)
        if revFlag:
            return 1/ans
        return ans

    def helper(self, x, n, res):
        if n == 1:
            return x * res

        if n % 2 == 1:
            res *= x
        
        x = x*x
        n = n // 2
        return self.helper(x, n, res)
