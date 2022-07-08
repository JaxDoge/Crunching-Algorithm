455. Assign Cookies



class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)

        if not m:
            return 0

        g.sort()
        s.sort()

        gp = sp = 0
        ans = 0
        while gp < n and sp < m:
            # if this cookie could content this child
            if s[sp] >= g[gp]:
                ans += 1
                gp += 1
                sp += 1
            else:
                sp += 1

        return ans