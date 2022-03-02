class Solution:
    def plusOne(self, s: str, j: int):
        s_list = list(s)
        if s_list[j] == '9':
            s_list[j] = '0'
        else:
            s_list[j] = str(int(s_list[j])+1)
        return "".join(s_list)

    def minusOne(self, s, j):
        s_list = list(s)
        if s_list[j] == '0':
            s_list[j] = '9'
        else:
            s_list[j] = str(int(s_list[j])-1)
        return "".join(s_list)

    def openLock(self, deadends: List[str], target: str) -> int:
        # record all dead ends in the visited hash set
        visited = set(deadends)
        # Bad case
        if '0000' in visited:
            return -1
        from collections import deque
        queue = deque()
        step = 0

        queue.append('0000')
        visited.add('0000')

        while len(queue) != 0:
            sub_loop_size = len(queue)

            for i in range(sub_loop_size):
                cur_pop = queue.popleft()

                if cur_pop == target:
                    return step

                # Add adjacent node in to queue
                for j in range(4):
                    up_pop = self.plusOne(cur_pop, j)
                    if up_pop not in visited:
                        queue.append(up_pop)
                        visited.add(up_pop)

                    down_pop = self.minusOne(cur_pop, j)
                    if down_pop not in visited:
                        queue.append(down_pop)
                        visited.add(down_pop)

            step += 1

        return -1




