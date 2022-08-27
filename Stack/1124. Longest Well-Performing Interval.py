1124. Longest Well-Performing Interval


# Monotonic Stack extreme practice
# 1. Basic solution, we use prefix sum array to locate the target i, j, such that i < j and preSum[i] < preSum[j]
# 2. the result is the largest j - i
# 3. but how should we iterate the preSum array with O(n) time complexity to find the i, j
# 4. Note that there are two fact: 1. for a given i, if i < j1 < j2 and preSum[i] < preSum[j2], we dont need check j1 anymore
# thus, we could search j from right to left in order to break loop earlier; 2. for a given j, if i1 < i2 < j and
# preSum[i1] < preSum[i2], i2 could be ignored, because no matter the relationship between preSum[i2] and preSum[j]
# i1 could always be better
# 5. based on second fact, a monotonic decreasing list could be composed of all possible i, which including 0 obviously:
# 6. For instance, in the given input, indeices [0, 5, 6] are all valid i, which denoted as stk
# 7. Note that, for each time we only need compare j(from right most index) with the right most possible i
# 8. Because if preSum[j] > preSum[i], great! we find a valid (i, j), but it could be better with next i: stk[-2]
# 9. if preSum[j] < preSum[i], this j could be totally rule out, because current preSum[i] is the smallest, thus
# this j no need compare with rest i
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # convert the hours to a new [-1, 1] array
        # what we are looking for is a subarray with sum larger than Zero
        newArr = []
        for h in hours:
            if h > 8:
                newArr.append(1)
            else:
                newArr.append(-1)

        preSum = [0 for _ in range(n + 1)]
        for i in range(n):
            preSum[i + 1] = preSum[i] + newArr[i]

        # Construct the monotonic stack
        stkI = []
        for idx, ps in enumerate(preSum):
            if not stkI or ps < preSum[stkI[-1]]:
                stkI.append(idx)

        # find the ans
        ans = 0
        for j in range(n, -1, -1):
            while stkI and preSum[j] > stkI[-1]:
                ans = max(ans, j - preSum[stkI[-1]])
                stkI.pop()

        return ans





# class Solution:
#     def longestWPI(self, hours: List[int]) -> int:
#         n = len(hours)
#         left, right = 0, 0
#         tiringDays = 0
#         ans = 0

#         while right < n:
#             if hours[right] > 8:
#                 tiringDays += 1

#             windowL = right - left + 1

#             if tiringDays > windowL - tiringDays:
#                 ans = max(ans, windowL)

#             right += 1

#         return ans