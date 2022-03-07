# Sieve of Eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        i = 2
        while i * i < n:  # Symmetry of factors
            if isPrime[i]:
                for j in range(i*i, n, i):  # 2*i, 3*i, ..., already scanned before
                    isPrime[j] = False
            i += 1

        return sum(isPrime) - 2 if sum(isPrime) >= 2 else 0
