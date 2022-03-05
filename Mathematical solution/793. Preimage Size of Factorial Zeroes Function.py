class Solution:
    # Return the tailing zeros of integer n
    def trailingZeroes(self, n: int) -> int:
        res = 0
        divisor = 5
        while divisor <= n:
            res += n // divisor
            divisor *= 5
        return res

    # Binary Search, the result could only be 5 or 0
    # Search left boundary
    # Note that, if the tailing zeros is k, the minial x is k, as there should be at least k element in factorial
    # in the same fashion, the maximal x is k*10, because it guarantee there are at least k '10's in factorial
    def preimageSizeFZF(self, k: int) -> int:
        low, high = k, k*10+1  # in case of k = 0
        while low <= high:
            mid = low + (high - low) // 2
            zeros = self.trailingZeroes(mid)
            if zeros == k:
                return 5
            elif zeros < k:
                low = mid + 1
            else:
                high = mid - 1

        return 0

