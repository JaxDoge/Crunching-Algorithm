216. Combination Sum III


# DFS
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Use used variable to record which integer is used 
        # used = 0
        res = []
        pathSum = 0

        def backtrack(restK, start, path):
            nonlocal n, res, pathSum
            if restK == 0:
                if pathSum == n:
                    res.append(path.copy())
                return

            for i in range(start, 10):
                # if there is no option
                if start > n - pathSum:
                    return

                # skip used number
                path.append(i)
                pathSum += i
                backtrack(restK - 1, i + 1, path)
                path.pop()
                pathSum -= i

        backtrack(k, 1, [])

        return res
