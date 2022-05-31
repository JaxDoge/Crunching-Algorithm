剑指 Offer 38. 字符串的排列


# DFS
class Solution:
    def permutation(self, s: str) -> List[str]:
        sList = list(s)
        sList.sort()
        n = len(s)

        res = []

        # memo record picked index, not the element, since there are potential duplicated element
        memo = set()

        def dfs(curPath):
            nonlocal res, memo, n, sList
            if len(curPath) == n:
                res.append("".join(curPath))
                return

            for i in range(n):
                if i in memo:
                    continue

                # to avoid duplicated curPath caused by duplicated characters exchanged they positions
                # we skip the char that is same as previous one and previous one has not been picked yet
                # in this way the duplicated element in curPath could maintain a "fixed" order as in the sList
                
                if i > 0 and sList[i] == sList[i - 1] and i - 1 not in memo:
                    continue

                curPath.append(sList[i])
                memo.add(i)
                dfs(curPath)
                curPath.pop()
                memo.remove(i)


            return

        dfs([])
        return res
