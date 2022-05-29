190. Reverse Bits





# bitwise operation
# add the last bite of n to the last bite of res, and shit n to the right by one
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1

        return res