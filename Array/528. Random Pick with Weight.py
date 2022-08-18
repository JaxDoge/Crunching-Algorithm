528. Random Pick with Weight


from random import randrange
class Solution:

    def __init__(self, w: List[int]):
        # Generate the preSum array
        n = len(w)
        preSum = [0] * (n + 1)
        for idx, weight in enumerate(w):
            preSum[idx + 1] = preSum[idx] + weight
        self.preSum = preSum

    def pickIndex(self) -> int:
        # find a random target number
        target = randrange(0, self.preSum[-1]) + 1

        # bisect
        left = 1 
        right = self.preSum[-1]

        while left < right:
            mid = left + (right - left) // 2

            if preSum[mid] == target:
                return mid - 1 

            elif preSum[mid] < target:
                left = mid + 1
            else:
                right = mid 

        return left - 1