621. Task Scheduler



# The coding is pretty simple, but the idea is extraodinarily tricky
# check this out https://leetcode.cn/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode-solution-ur9w/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter

        taskFreq = Counter(tasks)

        maxExec = max(taskFreq.values())

        maxETasks = 0
        for v in taskFreq.values():
            if v == maxExec:
                maxETasks += 1

        ans = (maxExec - 1) * (n + 1) + maxETasks
        
        return max(ans, len(tasks))
