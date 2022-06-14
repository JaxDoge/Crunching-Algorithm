剑指 Offer 45. 把数组排成最小的数



class Solution:
    def minNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        def udcmp(x, y):
            if x + y < y + x:
                return -1
            elif x + y > y + x:
                return 1
            else:
                return 0

        strNums = [str(x) for x in nums]
        strNums.sort(key = cmp_to_key(udcmp))
        return "".join(strNums)