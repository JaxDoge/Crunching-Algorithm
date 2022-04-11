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
        
        # 考虑除数为最小值的情况，之后二分查找可以将上界设为 -INT_MIN - 1，也就是 INT_MAX
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

        # 修改快速乘实现对任意 z 的判断，只用加法实现乘法，时间复杂度 O(logz)
        def quickAdd(y: int, z: int, x: int) -> bool:
            # x 和 y 是负数，z 是正数
            # 需要判断 z * y >= x 是否成立
            result, add = 0, y
            while z > 0:
                # 与运算判断奇偶性
                if (z & 1) == 1:
                    # 需要保证 result + add >= x， 注意 add 是负数，这个加和会随着迭代进行越来越小
                    # 较大的 Z 可能导致 add 过大溢出，故使用减法判断
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    # 需要保证 add + add >= x，否则提前结束，理论上可以不要这个判断，因为无论如何都要进入上一个分支，实际可以提高速度
                    if add < x - add:
                        return False
                    add += add
                # 不能使用除法
                z >>= 1
            return True

        # bisect, locate the right boundary
        # if bisection is failure, quotient should be zero
        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans



