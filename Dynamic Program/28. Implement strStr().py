28. Implement strStr()


# GO GO GO KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    	if not needle:
    		return 0
    	n = len(haystack)
    	m = len(needle)

    	dp = [[0]*256 for _ in range(m)]
    	dp[0][ord(needle[0])] = 1

    	X = 0
    	for j in range(1, m):
    		for c in range(0, 256):
    			dp[j][c] = dp[X][c]
    		dp[j][ord(needle[j])] = j + 1
    		X = dp[X][ord(needle[j])]

    	J = 0
    	for i in range(n):
    		J = dp[J][ord(haystack[i])]
    		if J == m:
    			return i - m + 1
    	return -1