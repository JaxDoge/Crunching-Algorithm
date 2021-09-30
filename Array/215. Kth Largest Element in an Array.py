215. Kth Largest Element in an Array

# Since a Binary Heap is a Complete Binary Tree, it can be easily represented as an array
# Priority Queue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    	def maxHeapify(array: List[int], root: int, heap_size: int):
    		left_node = root*2+1
    		right_node = root*2+2
    		largest = root

    		if left_node < heap_size and array[left_node] > array[largest]:
    			largest = left_node
    		if right_node < heap_size and array[right_node] > array[largest]:
    			largest = right_node
    		# 如果 root 比两个子节点小
    		if largest != root:
    			array[root], array[largest] = array[largest], array[root]
    		    maxHeapify(array, largest, heap_size)

        def buildHeap(array: List[int], heap_size: int):
        	# 由于排序堆的任意子树都是排序堆，因此要从最底层的树开始 heapify，但不需要从最底层的叶子节点开始
        	# 因为那没有排序的意义；具体来说是从倒数最后一个有叶子节点的根节点开始排（倒数第二层最右边的有叶子节点的
        	# 根节点，由于是完全二叉树，这个节点在队列中的位置必然是 length>>1 - 1
        	# 当然直接从最后索引开始也可以，效率问题

        	for node in range(heap_size//2-1,-1,-1):
        		maxHeapify(array, node, heap_size)

        heap_size = len(nums)
        buildHeap(nums, heap_size)

        # 开始弹出，弹出到第 k-1 次的时候 num[0] 就是第 kth largest number
        # 每次弹出要把最后一个 Index 对应的值放到 num[0]，于是可以从后遍历；未了保留信息，弹出的数和最后的数交换位置
        # 而不是直接丢弃，同时 heap_size - 1
        for index in range(len(nums)-1, len(nums)-k, -1):
        	nums[0], nums[index] = nums[index], nums[0]
        	heap_size -= 1
        	maxHeapify(nums, 0, heap_size)
        return nums[0]