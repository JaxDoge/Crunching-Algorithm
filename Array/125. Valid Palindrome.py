125. Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        clearS = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdecimal():
                clearS.append(s[i])
        if len(clearS) == 0:
            return True
        
        return self.check("".join(clearS))


    def check(self, s):
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i].lower() != s[j].lower():  # not case-sensitive
                return False
            i += 1
            j -= 1
        return True