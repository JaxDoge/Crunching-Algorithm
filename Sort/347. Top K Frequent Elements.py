347. Top K Frequent Elements


# Quick sort
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        num2F = defaultdict(int)

        for num in nums:
            num2F[num] += 1

        nFList = []
        for item in num2F.items():
            nFList.append(item)

        n = len(nFList)
        self.suffle(nFList, n)
        def sort(array, lo, hi, kTmp):
            if lo >= hi:
                return

            if kTmp == 0:
                return

            pi = self.partition(array, lo, hi)
            # Compare k with the length of LHS, which is hi - pi
            # Note that the numbers in each side are disordered
            # Note that if k == hi - pi, all LHS elements is the answer we want
            # if k == hi - pi + 1, all LHS elements plus pivote element is the answer
            if kTmp >= hi - pi + 1:
                sort(array, lo, pi - 1, kTmp - (hi - pi + 1))
            else:
                sort(array, pi + 1, hi, kTmp)

        sort(nFList, 0, n - 1, k)
        res = []
        for i in range(n - k, n):
            res.append(nFList[i][0])

        return res


    def partition(self, array, start, end):
        _, pivot = array[start]
        i = start
        j = end + 1

        while True:
            while True:
                i += 1
                if array[i][1] >= pivot or i == end:
                    break

            while True:
                j -= 1
                if array[j][1] <= pivot or j == start:
                    break

            if i >= j:
                break

            array[i], array[j] = array[j], array[i]

        array[j], array[start] = array[start], array[j]
        return j


    def suffle(self, array, n):
        from random import randint
        for i in range(n):
            rd = randint(i, n - 1)
            array[i], array[rd] = array[rd], array[i] 




# bucket sort
# O(n) space complexity
# O(n) time cmplexity

class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import defaultdict
        num2F = defaultdict(int)

        for num in nums:
            num2F[num] += 1

        maxF = 0
        for item in num2F.items():
            if item[1] > maxF:
                maxF = item[1]

        # create a bucket list with length maxF + 1
        bucket = [[] for _ in range(maxF + 1)]  # Watch out !! the nest list need initial in this way
        for nb, v in num2F.items():
            bucket[v].append(nb)

        res = []
        for i in range(maxF, -1, -1):  #  Start from maxF
            if len(res) >= k:
                break
            if len(bucket[i]) == 0:
                continue
            res.extend(bucket[i])

        return res



# Heapsort

# new info
# rewrite the python heapq to adapt the flexible cmp function

from heapq import heappop, heappush, heapify, heappushpop
class Myheap(object):
    def __init__(self, initial = None, key = lambda x: x):
        # heapq use the first element in a tuple to compare objects
        # so we could wrap the original objects in (key(item), selfIdx, item)
        self.key = key
        # (The extra self.index part is to avoid clashes when the evaluated key value is a draw and the stored value is not directly comparable - otherwise heapq could fail with TypeError)
        self.index = 0
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(initial)
            heapify(self._data)
        else:
            self._data = []

    def __len__(self):
        return len(self._data)

    def getTop(self):
        return self._data[0]

    def push(self, item):
        heappush(self._data, (self.key(item), self.index, item))
        self.index += 1

    def pop(self):
        return heappop(self._data)[2]

    def pushpop(self, item):
        outcast = heappushpop(self._data, (self.key(item), self.index, item))
        self.index += 1
        return outcast

    def getHeap(self):
        return self._data




class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import defaultdict

        num2F = defaultdict(int)
        for num in nums:
            num2F[num] += 1


        heapL = Myheap(key = lambda x: x[1])

        # add the first k elements in to heapL
        for item in num2F.items():
            if len(heapL) >= k:
                if heapL.getTop()[0] < item[1]:
                    heapL.pushpop(item)
                continue
            heapL.push(item)

        res = []
        for _, _, item in heapL.getHeap():
            res.append(item[0])
            
        return res

