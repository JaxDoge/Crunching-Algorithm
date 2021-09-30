7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x != 0:
            tmp = x % 10
            if x < 0 and tmp > 0:
                tmp -= 10
            # 判断翻转之后的数是否会溢出，考虑到我们只有 int(32)，可以提前一位判断是否大于 int.max // 10，
            # 因为x本身会被int限制，当x为正数并且位数和Integer.MAX_VALUE的位数相等时首位最大只能为2，
            # 所以逆转后不会出现res = Integer.MAX_VALUE / 10 && tmp > 2的情况，自然也不需要判断res==214748364 && tmp>7了，反之负数情况也一样

            if res > (2**31-1) // 10 or res < (-2**31+8) // 10:
                return 0

            res = res * 10 + tmp
            x = (x-tmp) // 10

        return res