202. Happy Number



class Solution:
    def __init__(self):
        self.memo = set()

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n in self.memo:
            return False

        self.memo.add(n)
        nextN = 0
        place = 1
        while n // place > 0:
            nextN += ((n // place) % 10) ** 2
            place *= 10

        return self.isHappy(nextN)