1523. Count Odd Numbers in an Interval Range



# 
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            if low % 2 != 0:
                return 1
            else:
                return 0
        if low % 2 == 0:
            low += 1

        if high % 2 == 1:
            high += 1

        nums = high - low + 1

        return nums // 2


