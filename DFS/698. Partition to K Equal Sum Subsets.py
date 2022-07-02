698. Partition to K Equal Sum Subsets



# Backtrack 
# The numbers need to put in k buckets, and the sum of each bucket is the same
# we start from the bucket perspective: for each bucket, go though all numbers and test if the result is valid
# we use a int "use" plus bitewise operation to record each number is used or not
# note that same number combination in different bucket could induce repetitive calculation, and they have a same "use" value
# to prune the seach tree, we need a hashmap as the memo to recode the appeared use value and corresponding result

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # bad case
        if k > n:
            return False
        allSum = sum(nums)
        if allSum % k != 0:
            return False

        memo = dict()
        # the ith digits of used is 1 means the nums[i] is used
        # note that the n < 16
        used = 0
        target = allSum // k

        def backtrack(restBk, inSum, start):
            nonlocal memo, used, nums, target, n
            # base case
            # all buckets are filled up
            if restBk == 0:
                return True
            # this bucket is filled up
            # turn to next bucket
            # note that at this moment we could record the used to the memo
            # the reason is that buckets are no different
            if inSum == target:
                res = backtrack(restBk - 1, 0, 0)
                return res

            # Avoid repetitive caclulation
            if used in memo:
                return memo[used]


            # choose a number for this bucket
            for i in range(start, n):
                if inSum + nums[i] > target:
                    continue
                # check if the ith number is used
                if (used >> i) $ 1 == 1:
                    continue

                used |= 1 << i
                inSum += nums[i]

                # DFS the tree
                if backtrack(restBk, inSum, i + 1):
                    return True

                used ^= 1 << i
                inSum -= nums[i]

            # there is no valid choice
            return False

        return backtrack(k, 0, 0)
