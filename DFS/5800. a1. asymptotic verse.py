
from collections import defaultdict
def createSong(n, k):
    res = float("inf")
    memo = defaultdict(bool)

    def backtrack(n, k, line):
        # Check memo
        if memo[(n, line)] == True:
            return False

        # Base case
        # Case 1
        if n == 0:
            res = min(res, line - 1)
            return True

        # Case 2: Bad case
        if n < line:
            return False

        # Case 3: If n could be perfectly arranged in this line
        if n % line == 0 and n / line <= k:
            res = min(res, line)
            return True

        # for this line, select one possible word count between 1~k, 0 is not permit
        for words in range(1, k+1):
            n = n - words * line
            line += 1
            backtrack(n, k, line)
            n += words
            line -= 1

        # Add to memo
        memo[(n, line)] = True

    backtrack(n, k, 1)

    return res




def dancingArray(arr):
    n = len(arr)
    l, r = 0, n - 1
    while l < r:
        # l points to the left most non-negative element
        while l < r and arr[l] < 0:
            l += 1
        # r points to the right most negative element
        while l < r and arr[r] >= 0: 
            r += 1

        if l < r:
            arr[l], arr[r] = arr[r], arr[l]

    return arr   





# Not just reduce to O(1) time complexity, but also dewindle to O(1) Space complexity
# auxiliary array
auxArr = [0] * K * 2

def merge(arr, left, mid, right):
    # Base case, self-merge - for rolling merge process
    if left == mid:
        return

    # If the maximum length of two subarray is greater than K * 2, then merge operation is trivial
    # Time complexity is O(1)
    if max(mid - left + 1, right - mid) > K * 2:
        return

    # Otherwise the merge operation time complexity is O(2K), which is O(1), too.
    for i in range(0, mid - left + 1):
        auxArr[i] = arr[left + i]
    for j in range(0, right - mid):
        auxArr[K + j] = arr[mid + 1 + j]    

    curP = left 
    ai, aj = 0, K

    while ai < mid - left + 1 and aj < right - mid:
        if auxArr[ai] <= auxArr[aj]:
            arr[curP] = auxArr[ai]
            ai += 1
        else:
            arr[curP] = auxArr[aj]
            aj += 1
        curP += 1

    while ai < mid - left + 1:
        arr[curP] = auxArr[ai]
        ai += 1
        curP += 1

    while aj < right - mid:
        arr[curP] = auxArr[aj]
        aj += 1
        curP += 1

def mergeSort(arr, left, right):
    # base case
    if left >= right:
        return

    # Case 1: length of arr is larger than K:
    if right - left + 1 > K:
        # Splitting the arr into n/K segments and recursively call mergerSort on each one
        # This case could at most occur once for all inputs.
        startP = left 
        preStartP = left
        while startP < right:
            endP = max(startP + K, right)
            mergeSort(arr, startP, endP)
            # Rolling merge, note that every segment will be merged twice except two end ones.
            merge(arr, preStartP, startP, endP)
            preStartP = startP
            startP = endP


    # Case 2: length of arr is smaller or equal to K:
    if right - left + 1 <= K:
        # Using regular merge sort
        mid = left + (right - left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)




def minHeapify(nums, root, d, heapSize):
    smallest = root  # assume root has the smallest value

    for j in range(1, d+1):
        child = d * root + j 

        if child < heapSize and nums[child] > nums[smallest]:
            smallest = child

    if smallest != root:
        nums[smallest], nums[root] = nums[root], nums[smallest]
        minHeapify(nums, smallest, d, heapSize)

def deleteMin(nums, heapSize, d):
    if heapSize < 1: return None

    tmp = nums[0]
    nums[0] = nums[heapSize - 1]
    heapSize -= 1

    minHeapify(nums, 0, d, heapSize)
    
    return tmp 
    








