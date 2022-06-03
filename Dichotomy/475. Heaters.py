475. Heaters



# dichotomy search the interval of all possible radius
# double pointer to scan two array to check the validity of possible radius
# use a check function to verify the radius candidate
# the principle of check function
# 1. if cand is larger than true answer, of course every house will be covered
# 2. we are not looking for the "closest" heater for every house, we are checking the validity of radius
# 3. So j points to the possible heater of house i
# 4. thus when heater[j] + r < house[i], it cannot be the one we are looking for. j need move forward, until heater[j] + r >= house[i] no matter 
# heater[j] is larger or smaller than house[i]
# 5. check if heat[j] - r <= house[i] <= heater[j] + r, if not, this radius is invalid
# 6. Note that we need sort houses and heaters, thus j could start from the position in the previous iteration

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        l, r = 0, 1e9   # 1e9 is the largest value of radius based on question constrains
        while l < r:
            mid = l + (r - l) // 2
            # if mid is valid, try to find a smaller one
            if self.check(houses, heaters, mid):
                r = mid
            else:
                l = mid + 1
        return int(l)



    def check(self, houses, heaters, radius):
        m = len(houses)
        n = len(heaters)
        j = 0
        for i in range(m):
            # find the j
            while j < n and heaters[j] + radius < houses[i]:
                j += 1
            if j < n and heaters[j] - radius <= houses[i] <= heaters[j] + radius:
                continue
            return False
        return True



# Well, there is another intuitive approach
# it's faster
# note that the j and i could be out bounded
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float('inf')
            leftDistance = house - heaters[i] if i >= 0 else float('inf')
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans