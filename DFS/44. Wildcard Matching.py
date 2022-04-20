44. Wildcard Matching



class Solution:
    def __init__(self):
        self.MEMO = {}
    
    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and p == '':
            return True
        elif s == '':
            # Check the characters in p
            for c in p:
                if c != '*':
                    return False
            return True

        elif p == '':
            return False

        return self.dfs(s, 0, p, 0)

    def dfs(self, s, i, p, j):
        # base case
        if j == len(p):
            return i == len(s)

        if i == len(s):
            # check if the rest of characters in p are all *
            for c in p[j:]:
                if c != '*':
                    return False
            return True

        # Check memo
        key = (i,j)
        if key in self.MEMO:
            return self.MEMO[key]

        # Carefully list all possible situation
        # 1. i match j, check next position
        if s[i] == p[j] or p[j] in {'?'}:
            res = self.dfs(s, i+1, p, j+1)
        # 2 j is *
        elif p[j] == '*':
            # 2.1 move i
            # 2.2 move j
            res = self.dfs(s, i+1, p, j) or self.dfs(s, i, p, j+1)
        else:
            res = False

        # record result in memo
        self.MEMO[key] = res

        return res


