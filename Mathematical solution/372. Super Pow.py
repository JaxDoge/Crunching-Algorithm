# Recursion

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        base = 1337

        # (a * b) % k = (a % k)(b % k) % k, this theorem holds not only for two factors but also for n factors
        # mypow return a % k
        def mypow(num, pow):
            num_mod = num % base
            res = 1
            for _ in range(pow):
                res *= num_mod
                res %= base
            return res

        # Base case
        if len(b) == 0:
            return 1

        last_num = b.pop()
        part1 = mypow(a, last_num)
        part2 = mypow(self.superPow(a, b), 10)
        return part1 * part2 % base

