1823. Find the Winner of the Circular Game



# Just recite it !!!
# 1-indexed
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(2, n + 1):
            winner = (k + winner - 1) % i + 1
        return winner


