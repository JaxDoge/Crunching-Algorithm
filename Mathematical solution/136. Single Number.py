"""
x ^ y = y ^ x
x ^ (y ^ z) = (x ^ y) ^ z  -----
x ^ 0 = x
x ^ y ^ y = x
x ^ x = 0
x ^ 0xFFFF = ~x
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
