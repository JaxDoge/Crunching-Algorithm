79. Word Search


# BackTrack

# BackTrack

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0],[0, 1],[-1, 0],[0, -1]]
        m, n = len(board), len(board[0])
        memo = set()

        # determine if the board[i][j] matches the word[k] character
        # determine if this selection is valid for word[k:]
        def isValid(i, j, k):
            nonlocal memo, directions, board, m, n

            # Base cases
        
            if board[i][j] != word[k]:
                return False

            if k >= len(word) - 1:
                return True    

            res = False
            # Backtrack, record thoes visited cells
            # The backtrack process could happen in for loop, but that would omit the entre cell. Need extra patch
            memo.add((i, j))
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                # new i j is valid?
                if (new_i, new_j) not in memo:
                    if new_i < m and new_i >= 0 and new_j < n and new_j >= 0:
                        res = isValid(new_i, new_j, k+1)
                        # we only need one valid path
                        if res: break
            memo.remove((i, j))
            return res


        for i in range(m):
            for j in range(n):
                if isValid(i, j, 0):
                    return True

        return False





