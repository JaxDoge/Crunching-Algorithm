10. Regular Expression Matching


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
    	m = len(s)
    	n = len(p)

    	from collections import defaultdict
    	memo = defaultdict(bool)
    	# double pointer
    	def dp(i, j):  
    		nonlocal memo, m, n, s, p
    		# base case
    		if j == n:
    			return i == m
    		if i == m:
    			# 只要p[j..]能够匹配空串，就可以算完成匹配。比如说s = "a", p = "ab*c*"，当i走到s末尾的时候，j并没有走到p的末尾，但是p依然可以匹配s。
    			if (n-j) % 2 != 0:
    				return False
    			# 检查 p 结尾是否为 x*y*z* 这种形式
    			for j in range(j, n, 2):
    				if p[j+1] != '*':
    					return False
    			return True

    		if (i,j) in memo:
    			return memo[(i,j)]

    		if s[i] == p[j] or p[j] == '.':
    			# j+1 是通配符
    			if j+1 < n and p[j+1] == '*':
    				# 可以匹配 i 多次或者 0 次
    				res = dp(i+1, j) or dp(i, j+2)
    			else:
    				res = dp(i+1, j+1)

    		else:
    			# 如果 j+1 是通配符，可以匹配 0 次
    			if j+1 < n and p[j+1] == '*':
    				res = dp(i, j+2)
    			# 匹配失败
    			else:
    				res = False
    		memo[(i,j)] = res
    		return memo[(i,j)]
    	return dp(0,0)