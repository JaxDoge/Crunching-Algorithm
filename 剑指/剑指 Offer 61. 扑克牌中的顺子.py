剑指 Offer 61. 扑克牌中的顺子



class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()

        # find the first none-zero number
        p = 0
        cnt = 0
        while p < 5:
            if nums[p] != 0:
                break
            cnt += 1
            p += 1
        
        if p >= 4:
            return True
        
        while p < 4:
            cur = nums[p]
            next = nums[p + 1]

            if next == cur:
                return False

            cnt -= next - cur - 1
            if cnt < 0:
                return False
            
            p += 1
        
        return True