74. Search a 2D Matrix


# bisection

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Searches vertically
        candList = [matrix[i][0] for i in range(m)]
        vCoor = self.bisection(target, candList)
        # bad cases
        if vCoor < 0:
            return False
        if matrix[vCoor][0] == target:
            return True

        # Search horizontally
        hCoor = self.bisection(target, matrix[vCoor])
        return matrix[vCoor][hCoor] == target

    def bisection(self, target, ls):
        left = 0
        right = len(ls) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if ls[mid] > target:
                right = mid - 1
            elif ls[mid] < target:
                left = mid + 1
            elif ls[mid] == target:
                return mid

        return right

