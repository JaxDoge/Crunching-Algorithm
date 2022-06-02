240. Search a 2D Matrix II



# 2 Dimension Dichotomy
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            ans = self.dichotomy(matrix[i], target)
            if target == matrix[i][ans]:
                return True

        return False

    def dichotomy(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return right    # if right is -1, we cannot find target in matrix


# Z shape scanning
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        # From the top right corner, we note that ever element on the left is strictly smaller than it
        # and ever elements below is strictly larger than it
        # thus we could move current element with following rules
        x = 0
        y = m - 1

        while x < n and y >= 0:
            if matrix[x][y] == target:
                return True

            # case 1, move current pointer one unit left, since matrix[x...n][y] are all larger than target
            elif matrix[x][y] > target:
                y -= 1
            # case 2, move one unit below, since matrix[x][0....y] are all smaller than target
            elif matrix[x][y] < target:
                x += 1

        return False


