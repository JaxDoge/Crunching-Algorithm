205. Isomorphic Strings



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        from collections import defaultdict
        sMapt = defaultdict(str)
        tMaps = defaultdict(str)

        for i in range(n):
            if s[i] in sMapt and sMapt[s[i]] != t[i]:
                return False
            if t[i] in tMaps and tMaps[t[i]] != s[i]:
                return False

            sMapt[s[i]] = t[i]
            tMaps[t[i]] = s[i]

        return True