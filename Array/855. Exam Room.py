855. Exam Room

class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)



# Using treemap to improve the time complexity
# leave() and seat() are O(logN) time complexity
# find the longest line segment in a ordered set

from sortedcontainers import SortedList
from functools import cmp_to_key

class ExamRoom(object):
    def udcmp(self, a: List[int], b: List[int]):
        dist_a = self.distance(a)
        dist_b = self.distance(b)
        # If they have same distance, descend sort intervals on their indices 
        if dist_a == dist_b:
            return b[0] - a[0]
        return dist_a - dist_b

    def __init__(self, N):
        self.N = N
        # map endpoints to the right line segment
        self.startMap = dict()
        # map endpoints to the left line segment
        self.endMap = dict()
        # main ordered list
        self.seg_container = SortedList(key = cmp_to_key(self.udcmp))
        # add dummy endpoints
        self.addInterval([-1, N])

    def removeInterval(self, intv: list):
        self.seg_container.remove(intv)
        del self.startMap[intv[0]]
        del self.endMap[intv[1]]

    def addInterval(self, intv: list):
        self.seg_container.add(intv)
        self.startMap[intv[0]] = intv
        self.endMap[intv[1]] = intv

    def distance(self, intv):
        # return the distance between potential seat point and endpoint, which is the middle point of line segment
        # except the far right one and far left one, add two exception judgements here 
        if intv[0] == -1:
            return intv[1]
        elif intv[1] == self.N:
            return self.N - intv[0] - 1
        else:
            return (intv[1] - intv[0]) // 2


    def seat(self):
        longest_line = self.seg_container[-1]
        start = longest_line[0]
        end = longest_line[1]

        # Consider the far endpoints
        if start == -1:
            student = 0
        elif end == self.N:
            student = self.N - 1
        else:
            student = (end - start) // 2 + start

        # bisect the longest line segment
        left_p = [start, student]
        right_p = [student, end]

        self.removeInterval(longest_line)
        self.addInterval(left_p)
        self.addInterval(right_p)
        
        # print the alloated seat of this student in passing
        return student

    def leave(self, p):
        # find the left and right intervals of p
        left_intv = self.endMap[p]
        right_intv = self.startMap[p]

        merge_intv = [left_intv[0], right_intv[1]]

        self.removeInterval(left_intv)
        self.removeInterval(right_intv)
        self.addInterval(merge_intv)



