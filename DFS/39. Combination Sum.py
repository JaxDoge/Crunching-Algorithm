39. Combination Sum

# DFS + pruning

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break

                # the path + [] will create a new copy, so the original list is untouched. Hence, no backtrack in the end
                # This question allow repetitive numbers, so the start index is still idx
                dfs(candidates, index, size, path + [candidates[index]], res, residue)
            return

        size = len(candidates)
        if size == 0:
            return []

        # Sort the candidates so that the pruning could take place before next recursion
        candidates.sort()

        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res

