139. Word Break


# Concatenate the wordDict to combine the s
# need a real dictionary of wordDict, key is the first letter of each word
# Backtrack
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = len(wordDict)

        wordMap = defaultdict(list)

        for i in range(m):
            fL = wordDict[i][0]
            wordMap[fL].append(wordDict[i])

        memo = {}
        def backtrack(start):
            nonlocal n, m, wordMap, s
            # base case
            if start == n:
                return True

            firstLetter = s[start]
            if (str(start), firstLetter) in memo:
                return memo[(str(start), firstLetter)]

            cands = wordMap[firstLetter]
            res = False
            for w in cands:
                span = len(w)
                targetW = s[start:start+span]
                if w == targetW:
                    res = backtrack(start+span)
                    if res:
                        break

            memo[(str(start), firstLetter)] = res
            return res

        return backtrack(0)

