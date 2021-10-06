76. Minimum Window Substring


# 滑动窗口
# 右指针移动寻找可行解，左指针移动优化当前可行解，优化完更新目前最优解，直到 right 移动到尽头
class Solution:
    def minWindow(self, s: str, t: str) -> str:
    	import collections
    	# 两个计数器，一个是目标计数字典，一个是目前 window 内的字符计数字典
    	need = collections.defaultdict(int)
    	window = collections.defaultdict(int)
    	for char in t:
    		need[char] += 1
    	
    	left = 0
    	right = 0
    	
    	# 记录目前 window 内已满足要求的字符数
    	valid = 0

    	# 记录最优解
    	start_from = 0
    	length = float('inf')

    	while right < len(s):
    		# 右移加入窗口的字符
    		char = s[right]
    		right += 1   # 注意 right 是开区间端点

    		# 是否是目标需要字符
    		if char in need:
    			window[char] += 1
    			# 该字符是否满足目标？
    			if window[char] == need[char]:
    				valid += 1  # 超过数量不计入

    		# 判断是否需要左移 left，是否遇到可行解需要优化
    		while valid == len(need):
    			# 开始更新最优解
    			if right - left < length:
    				start = left
    				length = right - left

    			c = s[left]
    			left += 1

    			# 是否是目标需要字符
    			if c in need:
    				# 是否目前刚好满足目标数量，移出后刚好不满足
    				if window[c] == need[c]:
    					valid -= 1
    				window[c] -= 1
    	if length <= len(s):
        	return s[start:(start+length)]
        return ""