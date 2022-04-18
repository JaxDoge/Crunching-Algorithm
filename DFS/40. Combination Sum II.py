40. Combination Sum II


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n == 0:
            return []

        candidates.sort()
        path = []
        ans = []

        self.dfs(candidates, 0, n, path, ans, target)

        return ans


    def dfs(self, cands, start, end, cur_path, res, target):
        # base case
        if target == 0:
            res.append(cur_path.copy())

        for idx in range(start, end):
            if target - cands[idx] < 0:
                break
            if idx > start and cands[idx - 1] == cands[idx]:
                continue

            cur_path.append(cands[idx])
            self.dfs(cands, idx+1, end, cur_path, res, target - cands[idx])
            cur_path.pop()


