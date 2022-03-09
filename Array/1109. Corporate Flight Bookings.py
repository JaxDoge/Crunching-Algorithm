1109. Corporate Flight Bookings


class Difference:
    def __init__(self, nums):
        n = len(nums)
        self.diff = []
        self.diff.append(nums[0])
        for i in range(1, n):
            self.diff.append(nums[i]-nums[i-1])

    def increment(self, i, j, val):
        self.diff[i] += val
        if j+1 < len(self.diff):
            self.diff[j+1] -= val

    def returnOrigin(self):
        res = [self.diff[0]]
        for i in range(1, len(self.diff)):
            res.append(res[i-1]+self.diff[i])
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        input_nums = [0] * n
        df = Difference(input_nums)

        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1
            seats = booking[2]

            df.increment(i, j, seats)

        return df.returnOrigin()