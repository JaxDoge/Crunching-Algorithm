301. Remove Invalid Parentheses


# integrated question
# count the minimum need-be-removed parentheses number
# check the validity of parentheses string
# DFS + prune the search tree

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        n = len(s)

        # find the minimum number of invalid left and right parentheses
        lmove = rmove = 0

        for i in range(n):
            if s[i] == "(":
                lmove += 1
            elif s[i] == ")":
                if lmove > 0:
                    lmove -= 1
                else:
                    rmove += 1

        # check the validity of a given string
        def isValid(ps):
            cnt = 0
            for p in ps:
                if p == "(":
                    cnt += 1
                elif p == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0


        # the dfs function represents the search state that given a string s and a start index "start"
        # there are lm left parentheses and rm right parentheses need to be removed
        # There are two pruning tactics:
        # 1. if this parenthese is the same as previous one, the result is the same
        # 2. if the remaining search length is shorter than the lm + rm, which means wrong track, just return the recursion
        res = []
        def dfs(s, start, lm, rm):
            nonlocal res
            # base case: all needless parentheses are reomved
            if lm == 0 and rm == 0:
                # check the validity of remaining string
                if isValid(s):
                    res.append(s)
                # Or just return
                return

            # choice a parenthese to remove from start index
            for i in range(start, len(s)):
                # prune tactic one:
                if i > start and s[i] == s[i - 1]:
                    continue

                # prune tactic two:
                if len(s) - i < lm + rm:
                    return

                # if s[i] is a left parenthese, and lm > 0    
                if lm > 0 and s[i] == "(":
                    dfs(s[0:i] + s[i + 1:], i, lm - 1, rm)

                if rm > 0 and s[i] == ")":
                    dfs(s[0:i] + s[i + 1:], i, lm, rm - 1)

        dfs(s, 0, lmove, rmove)
        return res

