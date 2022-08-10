1492. The kth Factor of n


# Enumerate number from 1 to sqrt(n)
# Then time complexity could be compressed to O(n)

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        factor = 1

        while factor * factor <= n:
            if n % factor == 0:
                count += 1
                if count == k:
                    return factor

            factor += 1

        factor -= 1

        # if n is a perfect square number
        # sqrt(n) would be duplicate factors
        if factor * factor == n:
            factor -= 1

        while factor > 0:
            if n % factor == 0:
                count += 1
                if count == k:
                    return n // factor
            factor -= 1

        return -1

