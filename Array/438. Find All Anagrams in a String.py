438. Find All Anagrams in a String


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
    	import collections
    	need = collections.defaultdict(int)
    	window = collections.defaultdict(int)
    	for char in p:
    		need[char] += 1

    	valid = 0
    	left = right = 0
    	ans = list()

    	while right < len(s):
    		char = s[right]
    		right += 1

    		if char in need:
    			window[char] += 1
    			if window[char] == need[char]:
    				valid += 1

    		while (right - left) >= len(p):
    			if valid == len(need):
    				ans.append(left)

    			c = s[left]
    			left += 1

    			if c in need:
    				if window[c] == need[c]:
    					valid -= 1
    				window[c] -= 1
    	return ans

