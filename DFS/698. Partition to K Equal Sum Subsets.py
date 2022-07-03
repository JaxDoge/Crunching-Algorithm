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
        # sort the nums
        nums.sort()

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
                memo[used] = res
                return res

            # Avoid repetitive caclulation
            if used in memo:
                return memo[used]


            # choose a number for this bucket
            for i in range(start, n):
                if inSum + nums[i] > target:
                    continue
                # check if the ith number is used
                if (used >> i) & 1 == 1:
                    continue

                if i > 1 and nums[i] == nums[i - 1]:
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




# Add another prune condition
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
        # sort the nums, for the last prune
        nums.sort()

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
                memo[used] = res
                return res

            # Avoid repetitive caclulation
            if used in memo:
                return memo[used]


            # choose a number for this bucket
            i = start
            while i < n:
            # for i in range(start, n):
                if inSum + nums[i] > target:
                    i += 1
                    continue
                # check if the ith number is used
                if (used >> i) & 1 == 1:
                    i += 1
                    continue

                used |= 1 << i
                inSum += nums[i]

                # DFS the tree
                if backtrack(restBk, inSum, i + 1):
                    return True

                used ^= 1 << i
                inSum -= nums[i]

                i += 1
                # Note that the nums is sorted, so if current number is not the correct selection
                # and the next number has the same value, we could skip the next one. There is no difference
                while i < n and nums[i] == nums[i - 1]:
                    i += 1

            # there is no valid choice
            return False

        return backtrack(k, 0, 0)