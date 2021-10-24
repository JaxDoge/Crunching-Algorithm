354. Russian Doll Envelopes

# 先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序。之后把所有的 h 作为一个数组，在这个数组上计算 LIS 的长度就是答案。
# 倒序保证了同宽度最多只取一个 高度
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    	length = len(envelopes)

    	import functools

    	def udcmp(a: list, b: list):
    		if a[0] == b[0]:
    			return b[1] - a[1]
    		else:
    			return a[0] - b[0]

    	# 按 width 排序，相同 width 按 height 倒排
    	sort_envelopes = sorted(envelopes, key = functools.cmp_to_key(udcmp))

    	# 对 height 列表寻找 LIS
    	height = []
    	for i in sort_envelopes:
    		height.append(i[1])

    	def lengthOfLIS(nums: list):
    		top = []
    		piles = 0

    		for ele in nums:
	    		left = 0
	    		right = piles-1
	    		while left <= right:
	    			mid = left+(right-left)//2
	    			if top[mid] >= ele:
	    				right = mid - 1
	    			elif top[mid] < ele:
	    				left = mid + 1
	    		if left == piles:
	    			piles += 1
	    			top.append(ele)
	    		else:
	    			top[left] = ele
	    	return piles


	    return lengthOfLIS(height)
