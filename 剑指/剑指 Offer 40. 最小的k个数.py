剑指 Offer 40. 最小的k个数


# bucket sort
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        # find the maximum
        maxN = 0
        for num in arr:
            if num > maxN:
                maxN = num

        # build the bucket array
        bucket = [0] * (maxN + 1)

        for num in arr:
            bucket[num] += 1

        res = []
        # ki = k
        for i in range(maxN + 1):
            if bucket[i] == 0:
                continue
            if res >= k:
                break
            else:
                res.extend([i] * bucket[i])

        return res[:k]

