977. Squares of a Sorted Array




# merge two array
# negative array and positive array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find the separator index
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] >= 0:
                break
            i += 1

        j = i - 1

        res = []
        while True:
            if j < 0 and i < n:
                res.extend(nums[i:n])
                break

            elif i >= n and j >= 0:
                res.append(-nums[j])
                j -= 1

            elif j < 0 and i >= n:
                break

            elif nums[i] <= abs(nums[j]):
                res.append(nums[i])
                i += 1
            else:
                res.append(-nums[j])
                j -= 1

        for i in range(n):
            res[i] = res[i] ** 2

        return res
