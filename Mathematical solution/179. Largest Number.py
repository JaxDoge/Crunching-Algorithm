179. Largest Number




# Greedy Algorithm
# Note that sorted take iterable item as the first parameter
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        strNums = map(str, nums)

        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b < b + a:
                return -1
            else:
                return 1

        strNums = sorted(strNums, key = functools.cmp_to_key(cmp), reverse = True)
        # Note that if there are only zeros in nums, the answer could be "00000", and it should be "0"
        return "".join(strNums) if strNums[0] != "0" else "0"