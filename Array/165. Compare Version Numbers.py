165. Compare Version Numbers



# Double points

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i = 0
        j = 0

        while i < m or j < n:  # loop through the longest string; scan one reversion for each time
            a = 0  # convert version to an integer
            while i < m and version1[i] != ".":
                a = a * 10 + ord(version1[i]) - ord("0")
                i += 1
            i += 1  # move point to the next number, or end of string

            b = 0
            while j < n and version2[j] != ".":
                b = b * 10 + ord(version2[j]) - ord("0")
                j += 1
            j += 1

            # Once a <> b, program return
            if a != b:
                return 1 if a > b else -1

        return 0

