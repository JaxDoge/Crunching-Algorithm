class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])

        target = '123450'

        # list board isn't convenient for BFS, so we recode it as string
        current = list()
        for a in range(m):
            for b in range(n):
                current.append(str(board[a][b]))
        current = ''.join(current)
        # Bad case
        if current == target:
            return 0

        # hashmap of neighbor indexs of each index
        neighbor_map = {0: [1, 3], 1: [0, 4, 2], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

        from collections import deque
        queue = deque()
        visited = set(current)
        queue.append(current)

        step = 0
        while len(queue) != 0:
            sub_loop_size = len(queue)
            for i in range(sub_loop_size):
                cur_pop = queue.popleft()
                if cur_pop == target:
                    return step

                # locate the index of character '0'
                zero_idx = 0
                while list(cur_pop)[zero_idx] != '0':
                    zero_idx += 1
                # swap the zero character with all neighbors
                for adj in neighbor_map[zero_idx]:
                    new_board = Solution.swap(list(cur_pop), adj, zero_idx)
                    if new_board not in visited:
                        queue.append(new_board)
                        visited.add(new_board)
            step += 1

        return -1

    @staticmethod
    def swap(cur_board, i, j):
        cur_board[i], cur_board[j] = cur_board[j], cur_board[i]
        return ''.join(cur_board)

