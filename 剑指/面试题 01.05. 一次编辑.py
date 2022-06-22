面试题 01.05. 一次编辑


# Spliting in several cases
# double pointers
# we tacitly accept the first string is longer, otherwise we could call a reverse function
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n = len(first)
        m = len(second)

        if m > n:
            return self.oneEditAway(second, first)

        if m == 0:
            return n <= 1

        f = s = 0

        while f < n and s < m:
            if first[f] != second[s]:
                break
            f += 1
            s += 1

        # Case 4: they are equal. Never think that count
        if f == n and s == m:
            return True

        # Case 1: extra letter in the middle of first string
        if s < m and n - m == 1:
            f += 1
            while f < n:
                if first[f] != second[s]:
                    return False
                f += 1
                s += 1
            return True

        # Case 2: Only one letter is different, so replace once
        if s < m and n == m:
            f += 1
            s += 1
            while f < n:
                if first[f] != second[s]:
                    return False
                f += 1
                s += 1                
            return True

        # Case 3: s is overflow
        if s == m:
            return f == (n - 1)

        return False
