29. Divide Two Integers


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0

        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        # rev 记录最终结果是否要取相反数
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev



        # decide the sign
        if dividend > 0 and divisor > 0:
            sign = 1
        elif dividend < 0 and divisor < 0:
            sign = 1
        else:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        remain = dividend
        quotient = 0
        while True:
            if remain < divisor:
                break
            remain -= divisor
            quotient += 1

        if sign == -1:
            return quotient - quotient -quotient
        else:
            return quotient


