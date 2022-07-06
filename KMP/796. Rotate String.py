796. Rotate String


# brutal force
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)

        if n != m:
            return False

        def check(s1, s2, p1):
            nonlocal n, m
            for i in range(m):
                if s1[p1] != s2[i]:
                    return False
                p1 = (p1 + 1) % n

            return True

        for j in range(n):
            # use the goal[0] as the alignment marker
            if s[j] != goal[0]:
                continue
            if check(s, goal, j):
                return True

        return False


# use defualt KMP substring match
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s