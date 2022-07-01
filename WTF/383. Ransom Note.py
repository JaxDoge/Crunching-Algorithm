383. Ransom Note


# Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        rC = Counter(ransomNote)
        mC = Counter(magazine)

        for l, n in rC.items():
            if l not in mC:
                return False
            if mC[l] < n:
                return False

        return True