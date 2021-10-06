3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	import collections
    	window = collections.defaultdict(int)

    	# 记录多少个字母有重复
    	repeat = 0
    	left = right = 0
    	ans = 0

    	while right < len(s):
    		char = s[right]
    		right += 1
    		# 判断是否加入后 window 有字符出现频次正好大于1
    		if window[char] == 1:
    			repeat += 1
    		window[char] += 1

    		if repeat == 0 and (right - left) > ans:
    			ans = right - left

    		while repeat > 0:
    			c = s[left]
    			left += 1

    			window[c] -= 1
    			if window[c] == 1:
    				repeat -= 1
    	return ans