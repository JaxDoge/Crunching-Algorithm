219. Contains Duplicate II



# sliding window
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        inWind = set()

        left = 0
        right = 0
        inWind.add(nums[left])

        while right < n and right - left < k:
            right += 1
            if right < n:
                if nums[right] in inWind:
                    return True
                else:
                    inWind.add(nums[right])

        while right < n - 1:
            inWind.remove(nums[left])
            left += 1
            right += 1
            if nums[right] in inWind:
                return True

            inWind.add(nums[right])


        return False