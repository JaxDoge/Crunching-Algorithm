66. Plus One



from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        carry = 1
        n = len(digits)

        for i in range(n-1, -1, -1):
            d = digits[i]
            if carry > 0:
                d_sum = d + carry
                if d_sum > 9:
                    res.appendleft(d_sum % 10)
                else:
                    res.appendleft(d_sum)
                    carry = 0
            else:
                res.appendleft(d)

        if carry > 0:
            res.appendleft(1)

        return list(res)
