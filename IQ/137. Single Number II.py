137. Single Number II


# Hashmap count the appearences
# Skip over

# DFA + Bitewise Operation
# Note that in Bitewise Operation, every bite change their status independently
# The key point is sum-up every 32-digits integer numbers' every bite(the number of 1s), then calculate the remainders of 3 
# of each bite must be zero or one(one means the result number has a one at this bite)

# the reminder of three is 0, 1, 2
# So there are three status
# using (one, two) to refer these status
# (0, 0), (0, 1), (1, 0)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0
        n = len(nums)
        for i in range(n):
            # update one first
            one = one ^ nums[i] & ~two
            two = two ^ nums[i] & ~one

        # the two must be zero at the end, because there is only one distinct number, thus the reminder could not be two finally
        return one