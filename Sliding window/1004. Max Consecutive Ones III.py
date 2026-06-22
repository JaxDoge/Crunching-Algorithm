1004. Max Consecutive Ones III


# Always maintain the biggest window size
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        l = r = 0
        while r < n:
            if nums[r] == 0:
                k -= 1
            r += 1

            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l





class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)

        pl = pr = 0

        zero_cnt = 0

        # Initial the window
        while zero_cnt < k and pr < n:
            if nums[pr] == 0:
                zero_cnt += 1
                
            pr += 1

        max_ans = pr - pl

        # move the window
        while pr < n:

            # if pr index point to ZERO, move pl to move the left most zero out of the window
            if nums[pr] == 0:
                pr += 1

                # ensure pl point to a ZERO
                while nums[pl] != 0:
                    pl += 1

                # Move pl one more time
                pl += 1

                max_ans = max(max_ans, pr - pl)
                continue

            else:
                pr += 1
                max_ans = max(max_ans, pr - pl)

        return max_ans