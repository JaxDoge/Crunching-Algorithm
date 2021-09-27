690. Employee Importance

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# BFS
import collections
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
    	staff_map = collections.defaultdict(Employee)
		helper_queue = collections.deque()
		for staff in employees:
			staff_map[staff.id] = staff

		helper_queue.append(staff_map[id])
		res = 0
		while helper_queue:
			pop_val = helper_queue.popleft()
			res += pop_val.importance
			for sub in pop_val.subordinates:
				helper_queue.append(staff_map[sub])

		return res
