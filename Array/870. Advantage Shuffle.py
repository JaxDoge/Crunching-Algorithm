870. Advantage Shuffle


# num2 本身保持原有顺序，使用其他变量存储副本，每次pop出最大值和对应的索引，可以考虑 heap queue
# num1 排序，并用双指针指向当下的最大最小值
# 如果 num1 最大值比 num2 最大值大，直接输出，如果较小，输出 num1 最小值
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	from heapq import heapify, heappop, heappush
    	length = len(nums1)

    	# num2 最大堆
    	max_heap = []
    	heapify(max_heap)
    	for i in range(length):
    		heappush(max_heap, (nums2[i]*(-1),i))

    	nums1.sort()
    	# double pointer
    	min = 0
    	max = length-1

    	res = [0]*length

    	while max_heap:
    		pop_pair = heappop(max_heap)
    		target_value = pop_pair[0]*(-1)
    		target_index = pop_pair[1]
    		if nums1[max] > target_value:
    			res[target_index] = nums1[max]
    			max -= 1
    		else:
    			res[target_index] = nums1[min]
    			min += 1

    	return res


