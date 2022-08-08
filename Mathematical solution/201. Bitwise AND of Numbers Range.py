201. Bitwise AND of Numbers Range


# Note that the bitewise left and right have common prefix
# and after the common prefix, all digits would be convert to zero
# thus we only need to preserve the common prefix, and change all rest digits to zero
# Brian Kernighan algorithm could change the right most 1 to 0 each time
# Note that the first different digits from left of left number is must be zero
# Thus once left number is larger or equal to right number, all different digits are set to zero
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= (right - 1)

        return right