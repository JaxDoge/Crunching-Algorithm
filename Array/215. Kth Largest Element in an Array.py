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
            # 如果 root 比两个子节点小，交換節點值，對受影響的子樹繼續執行 Heapify
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
        # 每次弹出要把最后一个 Index 对应的值放到 num[0]，于是可以从后遍历；為了保留信息，弹出的数和最后的数交换位置
        # 而不是直接丢弃，同时 heap_size - 1
        for index in range(len(nums)-1, len(nums)-k, -1):
            nums[0], nums[index] = nums[index], nums[0]
            heap_size -= 1
            maxHeapify(nums, 0, heap_size)
        return nums[0]


#  Quick Selection
#  This is an analogy of quick sort, but it is unnecessary to sort the whole list
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.shuffle(nums)
        low = 0
        high = len(nums) - 1
        k = len(nums) - k #  the kth largest element is the (n - k) th smallest one
        while low <= high:
            #  find a pivot index p
            p = self.partition(nums, low, high)
            if p < k:
                low = p + 1
            elif p > k:
                high = p - 1
            elif p == k:
                return nums[p]

        return -1

    def partition(self, ls, lo, hi):
        if lo == hi:
            return lo
        pivot = ls[lo]
        i = lo
        j = hi + 1
        while True:
            while True:
                i += 1
                if ls[i] >= pivot:
                    break
                if i == hi:
                    break

            while True:
                j -= 1
                if ls[j] <= pivot:
                    break
                if j == lo:
                    break

            if i >= j:
                break
            ls[i], ls[j] = ls[j], ls[i]

        ls[j], ls[lo] = ls[lo], ls[j]

        return j

    # shuffle original list to avoid the worst initial permutation
    def shuffle(self, init_nums):
        import random
        n = len(init_nums)
        for i in range(n):
            rd = random.randint(i, n - 1)
            init_nums[i], init_nums[rd] = init_nums[rd], init_nums[i]


    # def partition(self, arr, low, high):
    #     i = (low - 1)  # index of smaller element
    #     pivot = arr[high]  # pivot
    #
    #     for j in range(low, high):
    #
    #         # If current element is smaller than or
    #         # equal to pivot
    #         if arr[j] <= pivot:
    #             # increment index of smaller element
    #             i = i + 1
    #             arr[i], arr[j] = arr[j], arr[i]
    #
    #     arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #     return (i + 1)