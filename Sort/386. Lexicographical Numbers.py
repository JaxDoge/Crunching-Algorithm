386. Lexicographical Numbers


# Travel the lexicographical tree
# DFS
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(curNum):
            nonlocal ans, n
            if curNum > n:
                return

            ans.append(curNum)
            for i in range(10):
                dfs(curNum * 10 + i)

        for num in range(1, 10):
            dfs(num)

        return ans


# Iteration
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n

        num = 1
        for i in range(n):
            # put num in the right position
            ans[i] = num

            # find the next valid num
            if num * 10 <= n:
                num *= 10
            else:
                # if num += 1 is invalid
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1

        return ans
