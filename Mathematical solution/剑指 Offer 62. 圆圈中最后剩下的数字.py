剑指 Offer 62. 圆圈中最后剩下的数字

# f(n,m)=[(m-1)%n+x+1]%n
#       =[(m-1)%n%n+(x+1)%n]%n
#       =[(m-1)%n+(x+1)%n]%n
#       =(m-1+x+1)%n
#       =(m+x)%n



class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        winner = 0
        for i in range(2, n + 1):
            winner = (m + winner) % i
        
        return winner