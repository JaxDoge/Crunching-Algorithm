164. Maximum Gap



# Bucket Sort
# Note that the size of each bucket is based on the rule: the maximum gap cannot exists between elements located in the same bucket
# 
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        _max = max(nums)
        _min = min(nums)
        res = 0

        if n < 2:
            return 0

        bucketSize = max(1, (_max - _min) // (n - 1))  # bucketSize strictly larger than zero
        # Note that the real quotient could be a decimal rather than integer, so we need add a bucket after division
        # to make sure the largest number is covered
        bucketNum = (_max - _min) // bucketSize + 1
        # construct the bucket list, we just need the maximum and minimum of each bucket, so ...
        bucket = [[-1, -1] for _ in range(bucketNum)]
        # fill up the buckets
        for i in range(n):
            locale = (nums[i] - _min) // bucketSize
            if max(bucket[locale]) == -1:
                bucket[locale][0] = bucket[locale][1] = nums[i]

            else:
                bucket[locale][0] = min(bucket[locale][0], nums[i])
                bucket[locale][1] = max(bucket[locale][1], nums[i])

        # there could be empty buckets which should be excluded
        pre = -1
        for j in range(0, bucketNum):
            if bucket[j][0] == -1:
                continue
            if pre != -1:
                interG = bucket[j][0] - bucket[pre][1]
                res = max(res, interG)
            pre = j

        return res