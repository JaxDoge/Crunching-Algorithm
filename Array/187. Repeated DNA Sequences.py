187. Repeated DNA Sequences



# Hashmap
# slide a 10 digits lenght window
# count the occurrence of each substring
import collections
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)

        memo = collections.defaultdict(int)
        res = []

        for i in range(n - 9):
            j = i + 10
            curDNA = s[i:j]
            memo[curDNA] += 1

        for k, v in memo.items:
            if v > 1:
                res.append(k)

        return res
