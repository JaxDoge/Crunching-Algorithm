567. Permutation in String

# 滑动窗口双指针
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    	import collections
    	need = collections.defaultdict(int)
    	window = collections.defaultdict(int)
    	for char in s1:
    		need[char] += 1

    	valid = 0

    	left = 0
    	right = 0

    	# 左闭右开区间，结束时 right 指出数组
    	while right < len(s2):
    		char = s2[right]
    		right += 1

    		if char in need:
    			window[char] += 1
    			if window[char] == need[char]:
    				valid += 1

    		# 判断左指针是否需要收缩，注意当窗口长度和 s1 相等就要进入收缩的 while 循环，因为window最终必然等于这个长度; 最终结果判断在其中
    		while (right-left) >= len(s1):
    			if valid == len(need):
    				return True

    			c = s2[left]
    			left += 1
    			if c in need:
    				if window[c] == need[c]:
    					valid -= 1
    				window[c] -= 1

    	return False



