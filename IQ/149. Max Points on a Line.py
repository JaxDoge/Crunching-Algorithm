149. Max Points on a Line


# Lots of details 
# explicits all corner cases
# for a certain orginal point, other co-line points would share the same slope
# thus we could maintain a hashmap of slope value for each orginal points 

# Interesting part is, the gcd function could cover all corner cases
# which is amazing!
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # bad case
        if n <= 2:
            return n

        res = 0
        for i in range(n):
            # if the number of rest points is less than res or res is larger than half number of points
            # we could stop search, since the res wouldn't updated
            if res >= n - i or res > n // 2:
                break
            # use hashmap to record the number of points of each line - lines referred by the slope value
            slopeMap = defaultdict(int)
            maxL = 0 # max answer of this original point, but not include itself
            for j in range(i+1, n):
                a = points[i][0] - points[j][0]  # delta of x value
                b = points[i][1] - points[j][1]  # delta of y value

                # corner case 1, vertical of horizontal lines
                if a == 0:
                    b = 1
                elif b == 0:
                    a = 1
                # corner case 2, signed a or b
                else:
                    if b < 0:
                        a = -a
                        b = -b
                    # corner case 3, different expression of the same fraction; need reduction of fraction
                    g = self.gcd(a, b)
                    a /= g
                    b /= g
                key = "{0}_{1}".format(a, b)
                slopeMap[key] += 1
                maxL = max(maxL, slopeMap[key])

            res = max(res, maxL + 1)  # add original point itself

        return res

    # Euclidean algorithm
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a%b)

